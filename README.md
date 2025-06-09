# 📄 Resume Category Prediction App

AI-powered web app that predicts the job category of a given resume (PDF, DOCX, or TXT format) using a trained machine learning model.

Built with Streamlit, the app dynamically downloads ML models from Hugging Face Hub, so you don't have to store large files in the repo.

---

## 🚀 Demo

Live App: [https://airesumescrenning.streamlit.app/](https://airesumescrenning.streamlit.app/)

---

## 📌 Features

- Upload resumes in PDF, DOCX, or TXT formats  
- Automatic text extraction and cleaning  
- Predicts the job category of the resume using a machine learning classifier  
- Displays extracted text and predicted job category  
- Lightweight app — downloads models dynamically at runtime

---

## 🏗️ Installation

1. Clone the repository:  
    ```bash
    git clone https://github.com/AritriPodde2210/resume-category-prediction.git
    ```
2. Change directory to the project folder:  
    ```bash
    cd resume-category-prediction
    ```
3. Create and activate a Python virtual environment (optional but recommended):  
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```
4. Install dependencies:  
    ```bash
    pip install -r requirements.txt
    ```
5. Run the Streamlit app:  
    ```bash
    streamlit run app.py
    ```

---

## 📁 Project Structure

- 📁 models/ # Models downloaded dynamically at runtime
- 📄 app.py # Main Streamlit app
- 📄 requirements.txt # Python dependencies
- 📄 README.md # This file


---

## 🔧 Usage

- Open the app in your browser after running `streamlit run app.py`
- Upload your resume file (PDF, DOCX, or TXT)
- Wait for text extraction and prediction results
- View predicted job category and extracted text if needed

---

## ⚙️ How It Works

- Downloads pre-trained ML models from Hugging Face Hub dynamically
- Extracts raw text from uploaded resumes using PyPDF2, python-docx, or plain text decoding
- Cleans and preprocesses the extracted text
- Transforms text with TF-IDF vectorizer
- Predicts category with a pre-trained classification model
- Decodes predicted labels using label encoder

---

## 📜 License

This project is licensed under the MIT License.

---

If you want me to add any other section (like Contributing, Contact, or more detailed Usage), just say!  
And congrats again on deploying your app! 🎉
