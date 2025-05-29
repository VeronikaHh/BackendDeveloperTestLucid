from pydantic import BaseModel, constr

from app.constants import ONE_MB_STR_LEN


class CreatePostSchema(BaseModel):
    text: constr(max_length=ONE_MB_STR_LEN)

class GetPostSchema(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True
