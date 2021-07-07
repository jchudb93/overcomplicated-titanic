from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Titanic API"
    admin_email: str = "example@example.com"
    items_per_user: int = 50
    gcp_certificate_path: str

    class Config:
        env_file = ".env"
