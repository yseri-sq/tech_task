from application.services.request_service import RequestService
from infrastructure.repositories.sqlmodel_request_repository import (
    SQLModelRequestRepository
)


def get_request_service():
    repository = SQLModelRequestRepository()

    service = RequestService(repository)

    return service