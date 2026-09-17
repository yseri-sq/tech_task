from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    password: str


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: str
    device: str
    type: str
    description: str
    client: str
    status: str
