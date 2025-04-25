from fastapi import APIRouter # type: ignore
from fastapi.responses import JSONResponse # type: ignore
from app.utils.captcha import generate_captcha

router = APIRouter()

@router.get("/")
def generate_captcha_route():
    text, image_base64 = generate_captcha()
    return JSONResponse(content={"text": text, "image_base64": image_base64})