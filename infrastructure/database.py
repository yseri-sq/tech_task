from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///db.db")

def create_db():
    from domain.models.request import Request
    from domain.models.user import User

    SQLModel.metadata.create_all(engine) 