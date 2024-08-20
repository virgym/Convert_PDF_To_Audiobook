# PDF to Audiobook Converter

This project is a Python-based web application that converts PDF documents into audiobooks using text-to-speech (TTS) technology. The application leverages the `pyttsx3` library for TTS, `pypdf` for extracting text from PDFs, and `Gradio` for building an easy-to-use interface.

## Features

- **PDF to Audio Conversion**: Upload any PDF document, and the app will convert it into an audiobook.
- **Voice Selection**: Choose between a male and female voice for the narration.
- **Downloadable Output**: The generated audiobook is available for download in MP3 format.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pdf-to-audiobook.git
   ```
   
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the application:
    ```bash
    python pdf_to_audiobook.py
    ```
2. The app will open in your web browser. You can upload a PDF, choose the voice (male or female), and generate the audiobook.
<p align='center'>
  <img src='/UI.PNG' alt='Book Price Alert'/>
</p>

3. Once the conversion is complete, you can download the audiobook in MP3 format.
<p align='center'>
  <img src='/Capture.PNG' alt='Book Price Alert'/>
</p>

## Author
👩‍💻 Mutshinya Virginia Mudau

- GitHub: <a href='https://github.com/virgym' target='_blank'>@virgym</a>
- LinkedIn: <a href='https://www.linkedin.com/in/mutshinya-virginia-mudau-168a891b9/' target='_blank'>Mutshinya Virginia Mudau</a>

## License
<p>This project is licensed under the MIT License. See the LICENSE file for <a href 'LICENSE'> more details.</a></p>

## Acknowledgements
- Pyttsx3 for the text-to-speech functionality.
- Gradio for the easy-to-build web UI.
- pypdf for PDF text extraction.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.
