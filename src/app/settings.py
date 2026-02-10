from pathlib import Path
from pydantic import Field
from pydantic_settings import SettingsConfigDict, BaseSettings

data_path = Path(__file__).resolve().parent / "data"


class Settings(BaseSettings):
    # Environment variables

    app_name: str = Field(default="Course Materials Service", alias="NAME")
    debug: bool = Field(default=False, alias="DEBUG")
    address: str = Field(default="127.0.0.1", alias="ADDRESS")
    port: int = Field(default=8000, alias="PORT")
    reload: bool = Field(default=False, alias="RELOAD")

    model_config = SettingsConfigDict(
        env_file=".env.secret", env_file_encoding="utf-8", case_sensitive=True, extra="allow"
    )

    # Additional constants

    data_path: Path = data_path
    course_items_path: Path = data_path / "course_items.json"
    outcomes_path: Path = data_path / "outcomes.json"


settings = Settings()
