# Emotion Detection API

This is a simple API built with FastAPI for detecting emotions from text using a pre-trained NLP model.

## Features
- **POST /predict**: Predicts the emotion of a given text.
- **GET /health**: Checks the health status of the API.

---
### Prerequisites
- Python 3.8 or higher

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd emotion-api

### Create a virtual environment

python3 -m venv venv    # On Windows: python -m venv venv

source venv/bin/activate    # On Windows: venv\Scripts\activate

### Install dependencies

pip install -r requirements.txt

### Run

uvicorn app.main:app --reload
