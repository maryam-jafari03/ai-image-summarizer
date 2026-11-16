import os
import base64
from fastapi import FastAPI, UploadFile, File, Form
from openai import OpenAI
from dotenv import load_dotenv

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","my_django_project.settings")
django.setup()

from summarizer.models import Photo
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async

load_dotenv()

app = FastAPI()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

@app.post("/make_summarize")
async def summarize_image(
    user_info: str = Form(...),
    image: UploadFile = File(...)
):
    try:
        image_content = await image.read()

        image_size = len(image_content)

        base64_image = base64.b64encode(image_content).decode('utf-8')
        image_url = f"data:{image.content_type};base64,{base64_image}"

        user = (await sync_to_async(User.objects.get_or_create)(username="Mary"))[0]

        new_photo = await sync_to_async(Photo.objects.create)(
            format = image.content_type,
            size = image_size,
            dimensions = 0,
            owner = user
        )

        prompt_text = f"User Information: {user_info}\n\nPlease summarize the content of this image."

        response = client.chat.completions.create(
            model="google/gemma-4-26b-a4b-it:free",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_text},
                        {"type": "image_url", "image_url": {"url": image_url}},
                    ]
                }
            ],
            max_tokens=500
        )
        summary = response.choices[0].message.content
        return {
            "status": "success",
            "photo_id": new_photo.id,
            "summary": summary
        }

    except Exception as e:
       return {"status": "error", "message": str(e)}

