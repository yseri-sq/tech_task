from sqlmodel import create_engine, SQLModel

engine = create_engine("sqlite:///db.db")

def create_db():
    SQLModel.metadata.create_all(engine)

