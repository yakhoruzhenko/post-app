from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.models import users
from app.schemas import user
from app.services.hashing import Hash


def create(request: user.CreateUserRequest, db: Session) -> users.User:
    new_user = users.User(email=request.email, password=Hash.encrypt(request.password))
    db.add(new_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'User with login: {request.email} already exists')
    return new_user


def get_by_id(id: UUID, db: Session) -> users.User:
    user = db.query(users.User).filter(users.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with ID: {id} is not found')
    return user
