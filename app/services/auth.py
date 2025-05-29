from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.auth import get_password_hash, verify_password, create_token

class AuthService:
    def __init__(self, db: Session):
        self._db = db

    def signup_user(self, email: str, password: str):
        hashed = get_password_hash(password)
        user = User(email=email, hashed_password=hashed)
        self._db.add(user)
        self._db.commit()
        self._db.refresh(user)
        return create_token({"sub": email})

    def login_user(self, email: str, password: str):
        user = self._db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.hashed_password):
            return None
        return create_token({"sub": email})
