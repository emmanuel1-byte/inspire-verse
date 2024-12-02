import cloudinary
import dotenv

dotenv.load_dotenv()
import os

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_SECRET_KEY"),
)
from cloudinary.uploader import upload
from fastapi import HTTPException
import io
from gtts import gTTS


def upload_to_cloudinary(text: str, public_id: str):
    try:
        # Initialize a buffer
        buffer = io.BytesIO()

        tts = gTTS(text=text, lang="en")
        tts.write_to_fp(buffer)

        # Reset the buffer pointer
        buffer.seek(0)

        uploaded_file = upload(buffer, resource_type="auto", public_id=public_id)
        print(f"File uploaded succesfully {uploaded_file.get("public_id")}")

        return uploaded_file.get("url")
    except Exception as e:
        print(f"Error during Cloudinary upload: {e}")
        raise HTTPException(
            status_code=500,
            detail={"message": "File upload failed due to an unexpected error."},
        )
