from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).parent.parent


class AuthConfig(BaseSettings):

    secret_key: str

    model_config = SettingsConfigDict(
        env_prefix= "TEST_LUCID_",
        env_file=ROOT_DIR / Path(".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

auth_config = AuthConfig()
