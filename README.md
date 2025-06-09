# Resume Category Prediction App
AI-powered web app that predicts the job category of a given resume (PDF, DOCX, or TXT format) using a trained machine learning model.

✅ Built with Streamlit
✅ ML models hosted on HuggingFace Hub
✅ Dynamic model loading → no need to store large model files in GitHub
✅ Deployed on Streamlit Cloud

### 🚀 Demo
# 👉 Live App: https://airesumescrenning.streamlit.app/
### 📌 Features
Upload resumes in PDF, DOCX, or TXT formats

Automatic text extraction and cleaning

Predicts the job category of the resume using an ML classifier

Displays extracted text and predicted category

Lightweight app — models are downloaded dynamically from HuggingFace Hub

### ⚙️ How It Works
User uploads a resume file.

App extracts and cleans the text.

Pre-trained ML model classifies the resume into a job category.

The result is displayed on screen.

### Project Structure

📁 models/              # models downloaded dynamically at runtime
📄 app.py                # main Streamlit app
📄 requirements.txt      # Python dependencies
📄 README.md             # this file

### 🚀 To-Do (Future Enhancements)
 Show Top-3 probable categories with confidence scores

 Add progress bar while processing resume

 Improve app UI/UX with custom CSS

 Add more supported file formats (.doc)

 Deploy as a REST API (FastAPI + Streamlit frontend)
