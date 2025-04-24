from fastapi import FastAPI
from app.routes import generate

app = FastAPI(title="CAPTCHA Service API")

app.include_router(generate.router, prefix="/generate", tags=["captcha"])