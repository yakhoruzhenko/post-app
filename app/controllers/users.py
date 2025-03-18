from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from app.infra.database import get_db
from app.repositories import user as user_repo
from app.schemas import user
from app.services import auth

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('', status_code=status.HTTP_201_CREATED)
def sign_up(request: user.CreateUserRequest, db: Session = Depends(get_db)) -> dict[str, str]:
    '''
    Register a new user
    '''
    created_user = user.UserResponse.model_validate(user_repo.create(request, db))
    access_token = auth.create_access_token(data={'id': str(created_user.id)})
    return {'access_token': access_token, 'token_type': 'bearer'}
