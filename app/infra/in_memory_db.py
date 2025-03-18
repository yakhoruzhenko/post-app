from uuid import UUID

from app.models.posts import Post

POSTS: dict[UUID, list[Post]] = {}
