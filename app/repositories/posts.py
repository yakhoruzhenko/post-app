from copy import copy
import os
from uuid import UUID

from cachetools import TTLCache

from app.infra.in_memory_db import POSTS
from app.models import posts
from app.schemas.post import CreatePostRequest

MAX_CACHE_SIZE = float(os.getenv('MAX_CACHE_SIZE', '1024'))
CACHE_TTL = float(os.getenv('CACHE_TTL', '300'))

cache: TTLCache[UUID, list[posts.Post]] = TTLCache(maxsize=MAX_CACHE_SIZE, ttl=CACHE_TTL)  # ttl in seconds


def create(user_id: UUID, post_data: CreatePostRequest) -> posts.Post:
    new_post = posts.Post(content=post_data.content)
    user_posts = POSTS.get(user_id)
    if user_posts:
        user_posts.append(new_post)
    else:
        POSTS[user_id] = [new_post]
    cache.pop(user_id, None)
    return new_post


def get_all_by_user(creator_id: UUID) -> list[posts.Post]:
    if creator_id in cache:
        return cache[creator_id]
    else:
        posts_for_user = POSTS.get(creator_id, [])
        cache[creator_id] = copy(posts_for_user)
        return posts_for_user


def delete(creator_id: UUID, post_id: UUID) -> None:
    try:
        POSTS[creator_id] = [post for post in POSTS[creator_id] if post.id != post_id]
        cache.pop(creator_id, None)
    except KeyError:
        return None
