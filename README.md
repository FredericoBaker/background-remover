# Background Remover

Flask backend with a static HTML frontend for fast and efficient image background removal using [rembg](https://github.com/danielgatis/rembg). Simple, scalable, and user-friendly.

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/FredericoBaker/background-remover.git
   cd background-remover
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Linux/macOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the Flask backend**:
   ```bash
   python app.py
   ```
   You should see output like:
   ```
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

2. **Open the frontend**:
   - Simply open `index.html` in your browser, **or**
   - Serve it locally (e.g., `python -m http.server 8000`) and visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

3. **Upload an image** from the HTML page. The frontend will call the `/remove-bg` endpoint at `http://127.0.0.1:5000/remove-bg` by default and display the processed image.
