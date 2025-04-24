from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class CaptchaChallenge(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    solution: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_validated: bool = Field(default=False)
