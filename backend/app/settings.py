from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Environment variables

    app_name: str = Field(..., alias="NAME")
    debug: bool = Field(..., alias="DEBUG")
    address: str = Field(..., alias="ADDRESS")
    port: int = Field(..., alias="PORT")
    reload: bool = Field(..., alias="RELOAD")

    api_key: str = Field(..., alias="API_KEY")

    cors_origins: list[str] = Field(default=[], alias="CORS_ORIGINS")

    enable_interactions: bool = Field(..., alias="APP_ENABLE_INTERACTIONS")
    enable_learners: bool = Field(..., alias="APP_ENABLE_LEARNERS")

    db_host: str = Field(..., alias="DB_HOST")
    db_port: int = Field(..., alias="DB_PORT")
    db_name: str = Field(..., alias="DB_NAME")
    db_user: str = Field(..., alias="DB_USER")
    db_password: str = Field(..., alias="DB_PASSWORD")

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="allow",
    )


settings = Settings.model_validate({})
