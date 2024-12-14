import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os
import docx2txt
import PyPDF2
import tempfile

# Initialize the translator
translator = Translator()

# Function to translate English to French
def translate_to_french(word):
    try:
        if not word or word.strip() == "":
            return "Error: No text to translate."
        translated = translator.translate(word, src='en', dest='fr')
        return translated.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit app configuration
st.set_page_config(page_title="English to French Translator", layout="wide")
st.title("English to French Translator")

# Sidebar for additional settings
with st.sidebar:
    st.header("From Amr")
    language_option = "French"
    st.markdown("**More features coming soon🥳**")

# Columns for layout
col1, col2 = st.columns([2, 1])

# Input for English word
with col1:
    st.write("Enter the word or phrase you want to translate:")
    english_word = st.text_input("", placeholder="Type here...")

    # Upload document for translation
    st.write("Or upload a document to translate:")
    uploaded_file = st.file_uploader("Upload a Word or PDF document", type=["docx", "pdf"])

    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            try:
                # Using PdfReader instead of PdfFileReader
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                text = ""
                for page_num in range(len(pdf_reader.pages)):
                    page_text = pdf_reader.pages[page_num].extract_text()
                    if page_text:
                        text += page_text
                    else:
                        st.warning(f"No text extracted from page {page_num + 1}.")
                
                # If no text is extracted, set english_word to an empty string
                if not text:
                    st.warning("No text extracted from the PDF. Please check the document.")
                    english_word = ""
                else:
                    english_word = text

            except Exception as e:
                st.error(f"Error reading PDF: {e}")
                english_word = ""
                
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            try:
                text = docx2txt.process(uploaded_file)
                if not text:
                    st.warning("No text extracted from the Word document. Please check the document.")
                    english_word = ""
                else:
                    english_word = text
            except Exception as e:
                st.error(f"Error reading Word document: {e}")
                english_word = ""

# Translate and display result
if english_word:
    with col1:
        st.subheader("Translation")
        translation = translate_to_french(english_word)
        st.markdown(f"<div style='font-size: 24px; font-weight: bold; margin-top: 10px;'>**{english_word}** in French is:</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size: 32px; color: #4CAF50; font-weight: bold;'>{translation}</div>", unsafe_allow_html=True)

        # Convert both original and translated text to speech (TTS)
        if english_word and translation:
            # Convert English to speech
            tts_en = gTTS(english_word, lang='en')
            tts_fr = gTTS(translation, lang='fr')

            # Save to temporary files
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_en_file:
                tts_en.save(tmp_en_file.name)
                en_audio_file = tmp_en_file.name
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_fr_file:
                tts_fr.save(tmp_fr_file.name)
                fr_audio_file = tmp_fr_file.name

            # Play English audio
            st.subheader("Listen to the translation")
            st.audio(en_audio_file, format="audio/mp3", start_time=0)
            st.audio(fr_audio_file, format="audio/mp3", start_time=0)
            
            # Clean up temporary files
            os.remove(en_audio_file)
            os.remove(fr_audio_file)
