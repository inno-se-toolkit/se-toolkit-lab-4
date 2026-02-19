from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Environment variables

    app_name: str = Field(default="Learning Management Service", alias="NAME")
    debug: bool = Field(default=False, alias="DEBUG")
    address: str = Field(default="127.0.0.1", alias="ADDRESS")
    port: int = Field(default=8000, alias="PORT")
    reload: bool = Field(default=False, alias="RELOAD")

    api_token: str = Field(alias="API_TOKEN")

    enable_interactions: bool = Field(default=False, alias="ENABLE_INTERACTIONS")
    enable_learners: bool = Field(default=False, alias="ENABLE_LEARNERS")

    db_host: str = Field(default="localhost", alias="DB_HOST")
    db_port: int = Field(default=5432, alias="DB_PORT")
    db_name: str = Field(default="lab3", alias="DB_NAME")
    db_user: str = Field(default="postgres", alias="DB_USER")
    db_password: str = Field(default="postgres", alias="DB_PASSWORD")

    model_config = SettingsConfigDict(
        env_file=".env.secret",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="allow",
    )


settings = Settings.model_validate({})
