from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.configs import auth_config
from app.db.config import get_db
from app.models.user import User

ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password): return pwd_context.hash(password)
def verify_password(password, hashed): return pwd_context.verify(password, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now() + timedelta(hours=1)})
    return jwt.encode(to_encode, auth_config.secret_key, algorithm=ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, auth_config.secret_key, algorithms=[ALGORITHM])

def get_current_user(token: str = Depends(HTTPBearer()), db: Session = Depends(get_db)):
    try:
        payload = decode_token(token.credentials)
        user = db.query(User).filter(User.email == payload["sub"]).first()
        if not user:
            raise HTTPException(status_code=401)
        return user
    except: raise HTTPException(status_code=401)
