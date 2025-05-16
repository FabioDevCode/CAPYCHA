import os
from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from app.routes import api_router

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = FastAPI(
    title="CAPYCHA",
    version="1.0.0",
    description="CAPYCHA est un service de Captcha.",
    docs_url=None,
    redoc_url=None,
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
    }
)

if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="CAPYCHA - API Docs",
        swagger_favicon_url="/static/favicon.ico",
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

