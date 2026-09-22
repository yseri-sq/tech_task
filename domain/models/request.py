from sqlmodel import SQLModel, Field
from typing import Optional


class Request(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: str
    equipment: str
    fault_type: str
    description: Optional[str] = None
    client: str
    status: str
