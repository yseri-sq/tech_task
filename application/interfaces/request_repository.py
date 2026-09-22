from abc import ABC, abstractmethod


class RequestRepository(ABC):

    @abstractmethod
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
        pass