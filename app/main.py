from fastapi import FastAPI # type: ignore
from sqlmodel import SQLModel, create_engine # type: ignore

from app.routes import api_router

app = FastAPI(
    title="CAPYCHA",
    version="1.0.0",
    description="CAPYCHA est un service de Captcha.",
    redoc_url=None,
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
    }
)

# === Database config ===
DATABASE_URL = "sqlite:///./captcha.db"
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)

init_db()

# === Routers ===
app.include_router(api_router)

