from fastapi import APIRouter # type: ignore

from .generate import router as generate_router
from .project import router as project_router

api_router = APIRouter()

api_router.include_router(generate_router, prefix="/generate", tags=["captcha"])
api_router.include_router(project_router, prefix="/projects", tags=["projects"])
