from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "SALMAN SMM PANEL"
    APP_VERSION: str = "1.0.0"

    DATABASE_URL: str = ""

    TELEGRAM_BOT_TOKEN: str = ""
    ADMIN_TELEGRAM_ID: str = ""

    JWT_SECRET: str = ""
    API_SECRET: str = ""

    BASE44_API_URL: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
