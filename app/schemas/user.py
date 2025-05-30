from pydantic import BaseModel, EmailStr, constr

class CreateLoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=6)
