import flet as ft
import os

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000"

def main(page:ft.Page):
    gv = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)

    for i in range(500):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}", color="blue"),
                alignment= ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(2, ft.colors.AMBER_500),
                border_radius=ft.border_radius.all(8)
            )
        )
    page.update()

ft.app(target=main)
