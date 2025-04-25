from typing import Optional
from datetime import datetime
from pydantic import BaseModel # type: ignore


class ProjectCreate(BaseModel):
    domain: str


class ProjectRead(BaseModel):
    id: str
    domain: str
    public_key: str
    created_at: datetime
    updated_at: datetime


class ProjectUpdate(BaseModel):
    domain: Optional[str] = None
