import flet as ft
from core.dependencies import get_request_service
# page = ft.Page


def edit_page():
    order_num = ft.TextField(label="Enter №")
    result = ft.Column()

    def check_order(e):
        if not order_num.value:
            print("ERR")
            e.page.update()
            return
        
        request_id = int(order_num.value)

        service = get_request_service()
        request = service.get_request(request_id)

        if request is None:
            print("Not found")
        else:
            result.controls.append(
                ft.TextField(label="Client", value=request.client)
            )
            result.controls.append(
                ft.TextField(label="Equipment", value=request.equipment)
            )
            result.controls.append(
                ft.TextField(label="Faul Type", value=request.fault_type)
            )
            result.controls.append(
                ft.TextField(label="Description", value=request.description)
            )
            result.controls.append(
                ft.TextField(label="Status", value=request.status)
            )
        e.page.update()

    return ft.Container(
        content=
            ft.Column(
                controls=[
                    order_num,
                    ft.Button("Check", on_click=check_order),
                    result
                ]
            )   
        )