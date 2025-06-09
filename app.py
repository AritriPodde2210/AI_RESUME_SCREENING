import streamlit as st
st.set_page_config(page_title="Resume Category Prediction", page_icon="📄", layout="wide")

import requests
import os
import pickle

import docx  # for Word files
import PyPDF2  # for PDFs
import re

# Create models directory if not exists
os.makedirs("models", exist_ok=True)

def download_file(url, path):
    if not os.path.exists(path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, "wb") as f:
                f.write(response.content)
            st.write(f"Downloaded {path}")
        else:
            st.error(f"Failed to download {path}. HTTP Status: {response.status_code}")
    else:
        st.write(f"{path} already exists.")

# Correct raw URLs from Hugging Face to download actual binary files
download_file("https://huggingface.co/apodder/ai-resume-screening-models/resolve/main/clf.pkl", "models/clf.pkl")
download_file("https://huggingface.co/apodder/ai-resume-screening-models/resolve/main/tfidf.pkl", "models/tfidf.pkl")
download_file("https://huggingface.co/apodder/ai-resume-screening-models/resolve/main/encoder.pkl", "models/encoder.pkl")

@st.cache_resource
def load_models():
    with open('models/clf.pkl', 'rb') as f:
        svc_model = pickle.load(f)
    with open('models/tfidf.pkl', 'rb') as f:
        tfidf = pickle.load(f)
    with open('models/encoder.pkl', 'rb') as f:
        le = pickle.load(f)
    return svc_model, tfidf, le

svc_model, tfidf, le = load_models()

def cleanResume(txt):
    cleanText = re.sub(r'http\S+\s', ' ', txt)
    cleanText = re.sub(r'RT|cc', ' ', cleanText)
    cleanText = re.sub(r'#\S+\s', ' ', cleanText)
    cleanText = re.sub(r'@\S+', ' ', cleanText)
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub(r'\s+', ' ', cleanText)
    return cleanText.strip()

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

def extract_text_from_txt(file):
    file.seek(0)
    try:
        text = file.read().decode('utf-8')
    except UnicodeDecodeError:
        file.seek(0)
        text = file.read().decode('latin-1')
    file.seek(0)
    return text

def handle_file_upload(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif file_extension == 'docx':
        return extract_text_from_docx(uploaded_file)
    elif file_extension == 'txt':
        return extract_text_from_txt(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Upload PDF, DOCX, or TXT.")

def pred(input_resume):
    cleaned_text = cleanResume(input_resume)
    vectorized_text = tfidf.transform([cleaned_text])
    vectorized_text = vectorized_text.toarray()
    predicted_category = svc_model.predict(vectorized_text)
    predicted_category_name = le.inverse_transform(predicted_category)
    return predicted_category_name[0]

def main():
    # REMOVE this line below from here:
    # st.set_page_config(page_title="Resume Category Prediction", page_icon="📄", layout="wide")

    st.title("Resume Category Prediction App")
    st.markdown("Upload a resume in PDF, TXT, or DOCX format and get the predicted job category.")

    uploaded_file = st.file_uploader("Upload a Resume", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        try:
            resume_text = handle_file_upload(uploaded_file)
            st.success("Text extracted from the resume.")

            if st.checkbox("Show extracted text"):
                st.text_area("Extracted Resume Text", resume_text, height=300)

            st.subheader("Predicted Category")
            category = pred(resume_text)
            st.write(f"**{category}**")

        except Exception as e:
            st.error(f"Error processing the file: {str(e)}")


if __name__ == "__main__":
    main()
