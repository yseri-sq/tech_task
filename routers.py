import flet as ft
from datetime import datetime

def page_0():
    return ft.Container(
        content=
            ft.Column(
                controls=[
                    ft.Text("It's firts page", size=24, weight=ft.FontWeight.BOLD),
                    ft.Button("Like", icon=ft.Icons.FAVORITE, on_click=lambda e: print("Like"))
                ]
            )   
        )


def page_1():
    return ft.Container(
        content=
            ft.Column(
                controls=[
                    ft.Text("Second page")
                ]
            )
        )

def page_2():
    return ft.Container(
        content=
            ft.Column(
                controls=[
                    ft.Text("qwe")
                ]
            )
    )

dateField = ft.Ref[ft.TextField]()

def open_datepicker(e):
    picker = ft.DatePicker(
        on_change=set_date
    )

    e.page.overlay.append(picker)
    picker.open = True

def set_date(e):
    date = e.control.value
    dateM = date.astimezone().strftime('%d.%m.%Y')

    dateField.current.value = dateM
    dateField.current.update()

def dlg():
    return ft.AlertDialog(
        title="ADD",
        content=ft.Column(
            height=350,
            controls=[
                ft.Row(
                    controls=[
                        ft.TextField(label="№"),
                        ft.TextField(ref=dateField,
                                    label="date",
                                     read_only=True,
                                     on_click=open_datepicker)
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
                ft.Row(
                    controls=[
                        ft.CupertinoSlidingSegmentedButton(
                            controls=[
                                ft.Text("In work"),
                                ft.Text("Watting"),
                                ft.Text("Successed")
                            ]
                        ),
                    ft.Button(
                        "Add",
                        on_click=lambda _: print("asd")
                    )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ]
        )
    )