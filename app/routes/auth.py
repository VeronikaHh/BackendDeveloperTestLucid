from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_auth_service
from app.schemas.user import CreateLoginUserSchema
from app.services.auth import AuthService

router = APIRouter()

@router.post("/signup")
def signup(payload: CreateLoginUserSchema, auth_service: AuthService = Depends(get_auth_service)):
    return {"token": auth_service.signup_user(str(payload.email), payload.password)}

@router.post("/login")
def login(payload: CreateLoginUserSchema, auth_service: AuthService = Depends(get_auth_service)):
    token = auth_service.login_user(str(payload.email), payload.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": token}
