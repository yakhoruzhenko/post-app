import os
from typing import Any
from uuid import UUID

from pydantic import BaseModel, field_validator

MAX_POST_LENGTH = int(os.getenv('MAX_POST_LENGTH', '1_048_576'))


class CreatePostRequest(BaseModel):
    content: str

    @field_validator('content')
    def check_size_limit(cls, v: Any) -> Any:
        # Check the byte size of the string
        content_length = len(v.encode('utf-8'))
        if content_length > MAX_POST_LENGTH:
            raise ValueError("Content size exceeds 1MB")
        return v


class PostResponse(BaseModel):
    id: UUID
    content: str
