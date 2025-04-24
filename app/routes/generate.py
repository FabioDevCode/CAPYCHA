from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
def generate_captcha():
    return JSONResponse(content={"message": "CAPTCHA generation endpoint (coming soon)"})