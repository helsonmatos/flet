import flet as ft


def main(page: ft.Page):
    ola = ft.Text(value="ola mundo!", size=50)
    page.controls.append(ola)
    page.update()

ft.app(target=main)