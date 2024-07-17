import os

class Settings:
    SYNCTHING_API_KEY: str = os.getenv("SYNCTHING_API_KEY")
    SYNCTHING_URL: str = os.getenv("SYNCTHING_URL")
    LOCAL_DEVICE_ID: str = os.getenv("LOCAL_DEVICE_ID")
    EMAIL_HOST: str = os.getenv("EMAIL_HOST")
    EMAIL_PORT: int = int(os.getenv("EMAIL_PORT"))
    EMAIL_HOST_USER: str = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD: str = os.getenv("EMAIL_HOST_PASSWORD")
    EMAIL_FROM: str = os.getenv("EMAIL_FROM")
    EMAIL_TO: str = os.getenv("EMAIL_TO")

settings = Settings()
