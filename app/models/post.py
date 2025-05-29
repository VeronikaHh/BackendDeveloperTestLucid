from sqlalchemy import Column, Integer, ForeignKey, Text

from app.constants import ONE_MB_STR_LEN
from app.db.config import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    text = Column(Text(ONE_MB_STR_LEN))
    user_id = Column(Integer, ForeignKey("users.id"))
