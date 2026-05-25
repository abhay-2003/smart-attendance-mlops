from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str

    SIMILARITY_THRESHOLD: float

    EMBEDDINGS_PATH: str

    MLFLOW_TRACKING_URI: str

    class Config:

        env_file = ".env"


settings = Settings()