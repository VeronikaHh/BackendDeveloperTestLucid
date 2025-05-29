from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.config import get_db
from app.services.auth import AuthService
from app.services.post import PostService


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)

def get_post_service(db: Session = Depends(get_db)) -> PostService:
    return PostService(db)
