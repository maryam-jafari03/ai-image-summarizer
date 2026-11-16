# AI Image Summarizer Backend

A backend service built with FastAPI and Django ORM that receives images, processes them, and uses a Large Language Model (LLM) via OpenRouter to generate intelligent summaries based on user context.

## Features
- Receives images and user information via POST requests.
- Converts uploaded images to Base64 format for AI processing.
- Integrates with OpenRouter LLM to generate image summaries.
- Stores image metadata (format, size, owner) securely in a Django database.
- Asynchronous handling for high performance.

## Tech Stack
- **Backend Framework:** FastAPI
- **Database & ORM:** Django, SQLite
- **AI Integration:** OpenRouter API (using OpenAI Python client)
- **Language:** Python 3.x
- **Environment Management:** python-dotenv

##  How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/maryam-jafari03/ai-image-summarizer.git
   cd ai-image-summarizer


2. Install dependencies:
pip install fastapi uvicorn openai python-dotenv python-multipart django


3. Set up environment variables:
Create a .env file in the root directory and add your OpenRouter API key:
OPENROUTER_API_KEY=your_openrouter_api_key_here


4. Apply database migrations:
python manage.py migrate


5. Run the FastAPI server:
uvicorn main:app --reload --port 8080


6. Access the API documentation:
   Open your browser and go to: http://127.0.0.1:8080/docs
