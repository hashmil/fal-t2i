# Fal Text-to-Image Generator

This project is a Gradio-based web interface for generating images from text prompts using various AI models. It utilises the FAL AI API to generate images based on user input.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/hashmil/fal-t2i.git
   cd fal-t2i
   ```

2. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Set up your API key:
   - Copy and rename the `.env.example` file to `.env`:
     ```
     cp .env.example .env
     ```
   - Open the `.env` file and replace `your_api_key_here` with your actual FAL AI API key:
     ```
     FAL_KEY=your_api_key_here
     ```

## Running the Application

1. Ensure your virtual environment is activated (see step 3 in Setup).

2. Run the Python script:

   ```
   python3 main.py
   ```

3. Open your web browser and go to the URL displayed in the terminal (usually `http://127.0.0.1:7860`).

4. Use the interface to generate images:
   - Select a model from the dropdown menu
   - Enter a text prompt
   - Adjust other parameters as desired
   - Click "Generate Image"

## Features

- Multiple AI model options
- Customizable image size
- Adjustable inference steps
- Seed input for reproducible results
- Guidance scale control
- Safety checker toggle
- Support for generating multiple images
