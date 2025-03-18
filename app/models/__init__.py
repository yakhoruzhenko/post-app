from uuid import UUID, uuid4

from sqlalchemy import text
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(CHAR(36), primary_key=True, default=uuid4())
