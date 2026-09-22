import flet as ft
page = ft.Page

def requests_page():
    return ft.Container(
        content=
            ft.Column(
                controls=[
                    ft.Text("Second page")
                ]
            )
        )