from fastapi import APIRouter, HTTPException, BackgroundTasks, Request
from fastapi.responses import JSONResponse
from ..services.generative_ai.gemini import model
from ..services.generative_ai.prompt import (
    story_about_character_prompt,
    encouraging_vesrse_prompt,
)
from ..utils.rate_limit import limiter
import uuid
from ..services.upload.cloudinary import upload_to_cloudinary
import requests

verse = APIRouter(prefix="/api/inspire-verse")


@verse.get(
    "/story/search",
    tags=["Verse"],
    responses={404: {}},
)
@limiter.limit("5/minute")
async def get_bible_stories_about_bible_characters(
    character_name: str, background_tasks: BackgroundTasks, request: Request
):
    try:
        prompt = story_about_character_prompt(character_name)
        response = model.generate_content(prompt)
        if response.text.strip() == "None":
            raise HTTPException(
                status_code=404, detail={"message": "Bible character does not exist"}
            )

        file_unique_id = str(uuid.uuid4())
        background_tasks.add_task(upload_to_cloudinary, response.text, file_unique_id)

        return JSONResponse(
            content={"data": {"story": response.text, "audio_file_id": file_unique_id}},
            status_code=200,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": f"{str(e)}"})


@verse.get("/random-bible-quotes", tags=["Verse"])
@limiter.limit("5/minute")
def get_random_bible_quotes(request: Request):
    try:
        response = requests.get("https://bible-api.com/?random=verse")
        if response.status_code == 200:
            return JSONResponse(content={"data": {"quotes": response.json()}})
        raise HTTPException(
            status_code=response.status_code, detail={"message": "Error ocurred"}
        )
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail={"message": str(e)})

    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": str(e)})


@verse.get(
    "/topic-base-verse",
    tags=["Verse"],
    responses={400: {}},
)
@limiter.limit("5/minute")
def get_bible_verse_based_on_condition(
    condition: str, background_tasks: BackgroundTasks, request: Request
):
    try:
        prompt = encouraging_vesrse_prompt(condition)
        response = model.generate_content(prompt)

        if response.text.strip() == "None":
            raise HTTPException(
                status_code=400, detail={"message": "Please Enter a valid condition"}
            )

        file_unique_id = str(uuid.uuid4())
        background_tasks.add_task(upload_to_cloudinary, response.text, file_unique_id)

        return JSONResponse(
            content={
                "data": {
                    "bible_verse": response.text,
                    "audio_file_id": file_unique_id,
                }
            },
            status_code=200,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": str(e)})


@verse.get("/audio/{unique_id}", tags=["Audio"])
@limiter.limit("5/minute")
def get_audio_url(unique_id: str, request: Request):
    try:
        cloudinary_url = (
            f"https://res.cloudinary.com/dlvghwogf/video/upload/{unique_id}.mp3"
        )
        return JSONResponse(content={"data": {"audio_url": cloudinary_url}})
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": str(e)})
