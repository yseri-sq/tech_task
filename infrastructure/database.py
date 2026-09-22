from pathlib import Path

from sqlmodel import SQLModel, create_engine


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db.db"

engine = create_engine(
    f"sqlite:///{DB_PATH.as_posix()}"
)


def create_db():
    from domain.models.request import Request
    from domain.models.user import User

    SQLModel.metadata.create_all(engine)

    print("DATABASE:", DB_PATH)