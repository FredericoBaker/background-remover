# Background Remover

Ever tried to remove a background from an image and ended up trapped in a labyrinth of paywalls, account sign-ups, and "free trials" that expire faster than your patience? Yeah, same.  

So, instead of dealing with all that nonsense, I built my own background remover in **less than 20 minutes** using **Flask**, **rembg**, and **ChatGPT**. Honestly, finding a good library to handle background removal took longer.  

This is a solution that you can run locally - just upload your image, get the background removed, and move on with your life.  

### Features:
- 🚀 **Fast** – Background removal in seconds.  
- 🖼️ **Bulk support** – Process multiple images at once.  
- 📦 **Download ZIP** – Get all processed images in one click.  
- 🎯 **Simple** – No clutter, just results.  

Flask backend + static HTML frontend. Powered by [rembg](https://github.com/danielgatis/rembg).

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
