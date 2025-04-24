from fastapi import FastAPI
from app.routes import generate

from sqlmodel import SQLModel, create_engine
from app.models.base import CaptchaChallenge  # important pour que le modèle soit enregistré

app = FastAPI(title="CAPTCHA Service API")

# === Database config ===
DATABASE_URL = "sqlite:///./captcha.db"
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)

init_db()

# === Routers ===
app.include_router(generate.router, prefix="/generate", tags=["captcha"])
