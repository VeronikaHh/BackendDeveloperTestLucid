import time

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.post import Post
from app.models.user import User

POST_CACHE = {}

class PostService:
    def __init__(self, db: Session):
        self._db = db

    def add_post(self, text: str, user: User) -> int:
        if len(text.encode("utf-8")) > 1_000_000:
            raise HTTPException(status_code=413, detail="Payload too large")
        post = Post(text=text, user_id=user.id)
        self._db.add(post)
        self._db.commit()
        self._db.refresh(post)
        POST_CACHE.pop(user.id, None)
        return post.id

    def get_posts(self, user: User) -> list[Post]:
        cached = POST_CACHE.get(user.id)
        if cached and time.time() - cached[0] < 300:
            return cached[1]
        posts = self._db.query(Post).filter(Post.user_id == user.id).all()
        POST_CACHE[user.id] = (time.time(), posts)
        return posts

    def delete_post(self, post_id: int, user: User) -> None:
        post = self._db.query(Post).filter(Post.id == post_id, Post.user_id == user.id).first()
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        self._db.delete(post)
        self._db.commit()
        POST_CACHE.pop(user.id, None)
        return
