from fastapi import FastAPI
from app.routes import auth, post
from app.db.config import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(post.router)
