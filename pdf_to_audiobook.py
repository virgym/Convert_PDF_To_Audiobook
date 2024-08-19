import nltk
from nltk.tokenize import sent_tokenize
import pyttsx3
import gradio as gr
from gradio_pdf import PDF
from pypdf import PdfReader
from gradio.components import Audio, Dropdown

# Initialize the text-to-speech (TTS) engine
engine = pyttsx3.init()

# Set properties for the speech (optional)      
engine.setProperty('rate', 160)  # Set speed of speech (words per minute)
engine.setProperty('volume', 1.0)  # Set volume level (0.0 - 1.0)

# Download the necessary NLTK tokenizer model
nltk.download('punkt')

# Function to extract text from PDF to text
def extract_text_from_pdf(pdf_file_path):
    reader = PdfReader(pdf_file_path)
    text = ""

    # Extract text from all pages
    for page in reader.pages:
        text += page.extract_text()
        
    return text


# Function to convert text to speech
def text_to_speech_with_sentence_pause(pdf_file, voice_selection):
    voices = engine.getProperty('voices')
    selected_voice = voices[0].id if voice_selection == "Male" else voices[1].id
    engine.setProperty('voice', selected_voice)

    text = extract_text_from_pdf(pdf_file)

    # Replace line breaks and paragraph breaks with spaces to avoid long pauses
    text = text.replace('\n', ' ').replace('\r', ' ')
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

   # Clean sentences and ensure proper punctuation
    cleaned_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()  # Remove leading and trailing spaces
        if not sentence.endswith('.'):
            sentence += '.'  # Add a period if it doesn't already end with one
        cleaned_sentences.append(sentence)
    # print(cleaned_sentences)
    # Join the cleaned sentences back into a single string
    cleaned_text = '\n'.join(cleaned_sentences)  # Join with a space to separate sentences
    print(cleaned_text)

    # Define the output audio file path
    audio_file_path = "audiobook.mp3"

    # Convert the cleaned text to speech and save it to the audio file
    engine.save_to_file(cleaned_text, audio_file_path)
    engine.runAndWait() # Wait until the speech is done

    return audio_file_path

# Gradio interface
demo = gr.Interface(
    fn=text_to_speech_with_sentence_pause,  # The function to be called
    inputs=[
        PDF(label="Upload a PDF and convert to Audiobook"), 
        Dropdown(["Male", "Female"], label="Choose the voice")
    ],
    outputs=Audio(type="filepath", label="Audiobook"),  # Output component
    allow_flagging='never',
    theme=gr.Theme.from_hub('abidlabs/dracula_revamped')
)

# Launch the Gradio app
demo.launch(share=True)

# Stop the TTS engine if running
engine.stop()
