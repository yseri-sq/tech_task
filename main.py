import flet as ft
from presentation.dialogs.request_dialog import (
    create_request_dialog
)
from infrastructure.database import create_db

from presentation.pages.edit_page import edit_page
from presentation.pages.requests_page import requests_page
from presentation.pages.settings_page import settings_page

async def main(page: ft.Page):
    page.window.width = 1420
    page.window.height = 830
    page.title = "App"
    page.window.resizable = False
    page.window.maximizable = False
    

    body_content=ft.Column(
        alignment=ft.MainAxisAlignment.START,
        expand=True,
        controls=[]
    )

    def change_route(e):
        body_content.controls.clear()
        index = e.control.selected_index

        if index == 0:
            body_content.controls.append(edit_page())

        elif index == 1:
            body_content.controls.append(requests_page())

        elif index == 2:
            body_content.controls.append(settings_page())

        page.update()


    log_out = ft.Column(
        controls=[
            ft.IconButton(
                icon=ft.Icons.LOGOUT,
                on_click=lambda e: print("qwe")
            ),
        ],
        alignment=ft.MainAxisAlignment.END,
        expand=True
    )

    def show_dlg(e):
        page.show_dialog(create_request_dialog())



    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        on_change=change_route,
        leading=ft.FloatingActionButton(
            icon=ft.Icons.CREATE,
            content="Add",
            on_click=show_dlg
        ),
        pin_trailing_to_bottom=True,
        trailing=log_out,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.FAVORITE_BORDER,
                selected_icon=ft.Icons.FAVORITE,
                label="First",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.EDIT,
                selected_icon=ft.Icons.EDIT_ATTRIBUTES_OUTLINED,
                label="Second"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS,
                selected_icon=ft.Icons.EDIT_ATTRIBUTES_OUTLINED,
                label="Settings"
            )
        ],
    )

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Row(
                expand=True,
                controls=[
                    ft.SelectionArea(content=rail),
                    ft.VerticalDivider(width=1),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        expand=True,
                        controls=[body_content],
                    ),
                ],
            ), 
        )
    )

create_db()
ft.run(main=main)