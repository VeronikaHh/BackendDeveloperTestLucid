from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.configs import ROOT_DIR


class DatabaseConfig(BaseSettings):

    database_url: str

    model_config = SettingsConfigDict(
        env_prefix= "TEST_LUCID_",
        env_file=ROOT_DIR / Path(".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

database_config = DatabaseConfig()
engine = create_engine(database_config.database_url)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()
