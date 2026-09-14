import flet as ft

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