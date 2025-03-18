from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class User(Base):
    __tablename__ = 'users'
    email: Mapped[str] = mapped_column(String(512), nullable=False)
    password: Mapped[str] = mapped_column(String(512), nullable=False)
