from sqlmodel import Session

from application.interfaces.request_repository import RequestRepository
from domain.models.request import Request
from infrastructure.database import engine

class SQLModelRequestRepository(RequestRepository):
    def save(
        self,
        date,
        client,
        equipment,
        fault_type,
        description,
        status,
        assigned_to=""
    ):
        with Session(engine) as session:

            request = Request(
                date=date,
                client=client,
                equipment=equipment,
                fault_type=fault_type,
                description=description,
                status=status,
                assigned_to=assigned_to
            )

            session.add(request)
            session.commit()
            session.refresh(request)

            return request