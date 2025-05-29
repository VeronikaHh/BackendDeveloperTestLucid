from fastapi import APIRouter, Depends
from app.dependencies import get_post_service
from app.utils.auth import get_current_user
from app.services.post import PostService
from app.models.user import User
from app.schemas.post import GetPostSchema, CreatePostSchema

router = APIRouter()

@router.post("/post")
def add_post(
    payload: CreatePostSchema,
    current_user: User = Depends(get_current_user),
    post_service: PostService = Depends(get_post_service),
):
    post_id = post_service.add_post(payload.text, current_user)
    return {"postID": post_id}

@router.get("/posts", response_model=list[GetPostSchema])
def get_posts(
    current_user: User = Depends(get_current_user),
    post_service: PostService = Depends(get_post_service),
):
    return post_service.get_posts(current_user)

@router.delete("/post/{post_id}")
def delete_post(
    post_id: int,
    current_user: User = Depends(get_current_user),
    post_service: PostService = Depends(get_post_service),
):
    post_service.delete_post(post_id, current_user)
    return {"detail": "Post deleted"}
