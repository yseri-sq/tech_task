import flet as ft
from core.dependencies import get_request_service
# page = ft.Page

enter_num_col = ft.Ref[ft.Column]()
result_col = ft.Ref[ft.Column]()


def on_ecler_click():
    enter_num_col.current.visible = True
    result_col.current.visible = False

    enter_num_col.current.update()
    result_col.current.update() 

def edit_page():
    order_num = ft.TextField(label="Enter №")
    result = ft.Column(
        ref=result_col,
        controls=[]
    )
 
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
            result_col.current.controls.append(
                ft.Container(
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.TextField(label="Client", value=request.client),
                                            ft.TextField(label="Equipment", value=request.equipment)
                                        ]
                                    )                       
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.TextField(label="Faul Type", value=request.fault_type),
                                            ft.TextField(label="Description", value=request.description)
                                        ]
                                    )                       
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.TextField(label="Status", value=request.status),
                                            ft.Button("eclear", on_click=on_ecler_click),
                                            ft.Button("edit", on_click=...)
                                        ]
                                    )                      
                                ]
                            )
                        ]
                    )
                )
            )
        e.page.update()

    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    ref=enter_num_col,
                    controls=[
                        order_num,
                        ft.Button("Check", on_click=check_order),
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                result
                            ]
                        )
                    ]
                )
            ]
        )
    )