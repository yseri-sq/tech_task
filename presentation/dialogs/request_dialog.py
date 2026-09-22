
import flet as ft
from datetime import datetime

from core.dependencies import get_request_service


def create_request_dialog():

    date_field = ft.Ref[ft.TextField]()
    form_ref = ft.Ref[ft.Column]()

    def set_date(e):
        selected_date = e.control.value

        if selected_date:
            date_field.current.value = (
                selected_date.strftime("%d.%m.%Y")
            )

            date_field.current.update()

    def open_datepicker(e):
        picker = ft.DatePicker(
            on_change=set_date
        )

        e.page.overlay.append(picker)
        picker.open = True
        e.page.update()

    def on_submit(e):
        form = form_ref.current

        device_val = form.controls[1].controls[0].value
        type_val = form.controls[1].controls[1].value

        desc_val = form.controls[2].controls[0].value
        client_val = form.controls[2].controls[1].value

        status_segmented = form.controls[3].controls[0]
        status_index = status_segmented.selected_index

        status_map = {
            0: "In work",
            1: "Waiting",
            2: "Successed"
        }

        status_val = status_map.get(
            status_index,
            "In work"
        )

        final_date = date_field.current.value

        if not final_date:
            final_date = datetime.now().strftime("%d.%m.%Y")

        service = get_request_service()

        service.save_request(
            date=final_date,
            client=client_val,
            equipment=device_val,
            fault_type=type_val,
            description=desc_val,
            status=status_val
        )

        parent = form.parent

        while parent is not None:
            if parent.__class__.__name__ == "AlertDialog":
                parent.open = False
                break

            parent = parent.parent

        e.page.update()

    return ft.AlertDialog(
        title=ft.Text("ADD"),

        content=ft.Column(
            ref=form_ref,
            height=350,
            controls=[
                ft.Row(
                    controls=[
                        ft.TextField(label="№"),

                        ft.TextField(
                            ref=date_field,
                            label="date",
                            read_only=True,
                            on_click=open_datepicker
                        )
                    ]
                ),

                ft.Row(
                    controls=[
                        ft.TextField(label="device"),
                        ft.TextField(label="type")
                    ]
                ),

                ft.Row(
                    controls=[
                        ft.TextField(label="description"),
                        ft.TextField(label="customer")
                    ]
                ),

                ft.Container(expand=True),

                ft.Row(
                    controls=[
                        ft.CupertinoSlidingSegmentedButton(
                            selected_index=0,
                            controls=[
                                ft.Text("In work"),
                                ft.Text("Waiting"),
                                ft.Text("Successed")
                            ]
                        ),

                        ft.Button(
                            "Add",
                            height=50,
                            on_click=on_submit
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ]
        )
    )