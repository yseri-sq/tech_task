from application.interfaces.request_repository import RequestRepository


class RequestService:
    
    def __init__(self, repository: RequestRepository):
        self.repository = repository

    def get_request(self, request_id):
        from presentation.pages.edit_page import enter_num_col
        enter_num_col.current.visible = False
        enter_num_col.current.update()
        return self.repository.get_by_id(request_id)

    def save_request(
            self,
            date,
            client,
            equipment,
            fault_type,
            description,
            status,
            assigned_to=""
    ):
        return self.repository.save(
            date=date,
            client=client,
            equipment=equipment,
            fault_type=fault_type,
            description=description,
            status=status,
            assigned_to=assigned_to
        )
