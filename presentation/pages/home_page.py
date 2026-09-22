import flet as ft
page = ft.Page

def home_page():
    return ft.Container(
        content=
            ft.Column(
                controls=[
                    ft.Text("It's firts page", size=24, weight=ft.FontWeight.BOLD),
                    ft.Button("Like", icon=ft.Icons.FAVORITE, on_click=lambda e: print("Like"))
                ]
            )   
        )