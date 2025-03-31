from fastapi import FastAPI, File, UploadFile
import fitz  # PyMuPDF for PDF processing
import os
from transformers import pipeline

app = FastAPI()

# Create an "uploads" folder if it doesn't exist
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load an NLP model (free model from Hugging Face)
requirement_extractor = pipeline("text-classification", model="facebook/bart-large-mnli")

@app.get("/")
def home():
    return {"message": "Backend is running!"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
    # Save file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text from PDF
    extracted_text = extract_text(file_path)

    # Extract requirements using NLP
    extracted_requirements = extract_requirements(extracted_text)

    return {"filename": file.filename, "requirements": extracted_requirements}

def extract_text(file_path):
    """Extract text from a PDF file."""
    doc = fitz.open(file_path)
    text = "\n".join([page.get_text() for page in doc])
    return text

def extract_requirements(text):
    """Use NLP to extract key functional and non-functional requirements."""
    predictions = requirement_extractor(text, return_all_scores=True)
    return predictions
