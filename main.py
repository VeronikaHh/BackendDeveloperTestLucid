from fastapi import FastAPI
from app.controllers import auth_controller, post_controller
from app.db.config import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_controller.router)
app.include_router(post_controller.router)
