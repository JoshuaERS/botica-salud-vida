from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = "cambiar-en-produccion"
    DATABASE = BASE_DIR / "database.db"
    UPLOAD_FOLDER = BASE_DIR / "uploads"
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024

