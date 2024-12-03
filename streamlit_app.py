import streamlit as st
import os
import docx2txt
import PyPDF2
import pyperclip
import tempfile

# Streamlit app configuration
st.set_page_config(page_title="Document Processor", layout="wide")
st.title("Document Processor")

# Sidebar for additional settings
with st.sidebar:
    st.header("From Amr")
    st.markdown("**More features coming soon🥳**")

# Columns for layout
col1, col2 = st.columns([2, 1])

# Input for English word
with col1:
    st.write("Enter the word or phrase you want to process:")
    input_word = st.text_input("", placeholder="Type here...")

    # Upload document for processing
    st.write("Or upload a document to process:")
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
                
                # If no text is extracted, set input_word to an empty string
                if not text:
                    st.warning("No text extracted from the PDF. Please check the document.")
                    input_word = ""
                else:
                    input_word = text

            except Exception as e:
                st.error(f"Error reading PDF: {e}")
                input_word = ""
                
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            try:
                text = docx2txt.process(uploaded_file)
                if not text:
                    st.warning("No text extracted from the Word document. Please check the document.")
                    input_word = ""
                else:
                    input_word = text
            except Exception as e:
                st.error(f"Error reading Word document: {e}")
                input_word = ""

    # Display processed text
    if input_word:
        st.write("Processed Text:")
        st.text_area("", input_word, height=300)
