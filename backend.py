from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from io import BytesIO
from rembg import remove
import zipfile

app = Flask(__name__)
CORS(app)  # Enable CORS so our frontend can call this API

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    # Try to get files from the 'images' key.
    files = request.files.getlist('images')
    # If not found, check for a single file with the key 'image'
    if not files:
        file = request.files.get('image')
        if file:
            files = [file]
        else:
            return jsonify({'error': 'No image uploaded'}), 400

    # If only one image is uploaded, process and return it directly.
    if len(files) == 1:
        file = files[0]
        input_data = file.read()
        try:
            output_data = remove(input_data)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        return send_file(
            BytesIO(output_data),
            mimetype='image/png',
            as_attachment=True,
            download_name='output.png'
        )
    else:
        # Multiple images: process each and package them into a ZIP archive.
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
            for idx, file in enumerate(files, start=1):
                input_data = file.read()
                try:
                    output_data = remove(input_data)
                except Exception as e:
                    return jsonify({'error': f"Error processing {file.filename}: {str(e)}"}), 500

                # Use the original filename (ensuring a .png extension) or a default name.
                filename = file.filename if file.filename else f'image_{idx}.png'
                if not filename.lower().endswith('.png'):
                    filename = filename.rsplit('.', 1)[0] + '.png'
                zf.writestr(filename, output_data)
        zip_buffer.seek(0)
        return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name='processed_images.zip'
        )

if __name__ == '__main__':
    app.run(debug=True)
