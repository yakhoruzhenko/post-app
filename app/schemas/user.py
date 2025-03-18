from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from app.schemas.post import PostResponse


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=512)

    @field_validator('email', mode='after')
    @classmethod
    def lower_case(cls, value: str) -> str:
        return value.lower()
