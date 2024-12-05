# 🎈 English to French Translator
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://blank-app-template.streamlit.app/)](https://6gcqyb9gx9wu46qkuh5dua.streamlit.app/)


A fully interactive Streamlit-based application designed to translate English text or documents into French, complete with text-to-speech functionality. This project is an ideal tool for anyone looking to learn French or to easily translate content from English, offering support for individual words, entire paragraphs, and even document uploads.

## Table of Contents
- [Features](#features)
- [Live Demo](#live-demo)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technical Overview](#technical-overview)
- [Known Limitations](#known-limitations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Features
- **Real-time Translation**: Translate English text or uploaded documents (PDF or Word) to French instantly.
- **Document Uploads**: Supports translation of PDF and Word documents, ideal for larger pieces of text.
- **Text-to-Speech**: Listen to both the original English text and the French translation, enhancing learning.
- **Streamlit Interface**: A clean, responsive UI that is accessible to users with any level of technical expertise.
- **Error Handling**: Smart error handling for empty inputs, unsupported document types, or issues with translation and text extraction.

## Live Demo
A live version of this translator is hosted at [Streamlit Cloud](https://share.streamlit.io/imnotamr/English-to-French-app-using-STREAMLIT/main/app.py). Visit the link to try the translator directly in your browser.

## Getting Started
These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites
Make sure you have Python 3.7 or newer installed. Also, it's recommended to create a virtual environment to manage dependencies.

- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/imnotamr/English-to-French-app-using-STREAMLIT.git
   cd English-to-French-app-using-STREAMLIT
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## Configuration
- The app uses Google Translate API (`googletrans`) and Google Text-to-Speech (`gTTS`). Both require an active internet connection.
- Optional: You may configure the app settings through Streamlit's sidebar, including future language support.

## Usage
1. **Text Input**: Enter any English word or phrase you want to translate.
2. **Document Upload**: Upload a Word (.docx) or PDF document for translation.
3. **Listen to Audio**: Play the text-to-speech versions for both the original and translated text.

### Example Workflow
- Start the Streamlit server using `streamlit run app.py`.
- Enter the text "Hello, how are you?" in the input box.
- Click the "Translate" button to get the French translation "Bonjour, comment ça va?".
- Click the audio buttons to hear the translation in both languages.

## Project Structure
- **app.py**: Main Streamlit app file containing the application logic.
- **requirements.txt**: File containing all Python dependencies.
- **README.md**: Detailed information about the project.
- **.gitignore**: Lists files and folders to be ignored by git.

## Technical Overview
This application is built using several key technologies:
- **Streamlit** for the front-end interface.
- **Googletrans**: A Python library that provides a simple interface to Google Translate API.
- **gTTS**: The Google Text-to-Speech library used for converting text to audio files.
- **PyPDF2 & docx2txt**: Libraries for extracting text from PDF and Word documents.

#### Core Functions
- `translate_to_french(word)`: Handles translation from English to French using Google Translate.
- **Document Handling**: PDF and DOCX files are read and processed to extract translatable content, leveraging PyPDF2 and docx2txt.

## Known Limitations
- **Translation Accuracy**: Googletrans may not provide 100% accurate translations.
- **PDF Scans**: The app does not support OCR for scanned PDFs. Text extraction may fail if the document is a scanned image.
- **Audio Quality**: The quality of the gTTS audio might vary based on network speed.

## Future Enhancements
- **Multi-Language Support**: Expand translations to support more languages besides French.
- **OCR for PDF Scans**: Use OCR technology to enable text extraction from scanned documents.
- **User Authentication**: Add user accounts to save translations and access history.
- **Customizable Voice**: Allow users to select different voices for text-to-speech.

## Contributing
Contributions are welcome! Please open an issue or create a pull request for any feature requests or bug fixes.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
Developed by **Amr**. For any queries, feel free to reach out on [GitHub](https://github.com/imnotamr).

---
Thank you for using the English to French Translator! I hope this project helps you in your journey of learning languages. If you have any suggestions for improvements, please feel free to contribute or reach out.


