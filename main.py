import flet as ft
from routers import page_0, page_1, page_2

async def main(page: ft.Page):
    page.window.width = 1420
    page.window.height = 830
    page.title = "App"


    body_content=ft.Column(
        alignment=ft.MainAxisAlignment.START,
        expand=True,
        controls=[]
    )

    def change_route(e):
        body_content.controls.clear()
        index = e.control.selected_index

        if index == 0:
            body_content.controls.append(page_0())

        elif index == 1:
            body_content.controls.append(page_1())

        elif index == 2:
            body_content.controls.append(page_2())

        page.update()


    log_out = ft.Button(icon=ft.Icons.LOGOUT, on_click=...)    


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
            on_click=lambda e: print("FAB")
        ),
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
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.LOGOUT,
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


ft.run(main=main)