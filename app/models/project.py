from sqlmodel import SQLModel, Field # type: ignore
from typing import Optional
from datetime import datetime
import uuid


class Project(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    domain: str
    public_key: str = Field(default_factory=lambda: str(uuid.uuid4()))
    private_key: str = Field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
