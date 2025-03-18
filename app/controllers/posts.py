from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status

from app.models.posts import Post
from app.models.users import User
from app.repositories import posts
from app.schemas import post
from app.services.auth import get_current_user

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router.post('', status_code=status.HTTP_201_CREATED)
def add_post(request: post.CreatePostRequest,
             current_user: User = Depends(get_current_user)) -> None:
    '''
    Create a new post
    '''
    posts.create(current_user.id, request)


@router.get('/own', status_code=status.HTTP_200_OK)
def get_own_posts(current_user: User = Depends(get_current_user)) -> list[Post]:
    '''
    Retrieve all posts for the current user
    '''
    return posts.get_all_by_user(current_user.id)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete(id: UUID, current_user: User = Depends(get_current_user)) -> None:
    posts.delete(current_user.id, id)
