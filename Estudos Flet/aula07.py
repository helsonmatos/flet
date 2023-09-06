import flet as ft

def main(page:ft.Page):
    page.add(
        ft.Text("ola mundo", size=30, color="red"),
        ft.Container(
        width=400,
        height=100,
        bgcolor=ft.colors.AMBER_100
        ),
        ft.Container(
        width=400,
        height=100,
        bgcolor=ft.colors.AMBER_100
        ),
        ft.TextField(label="Digite aqui")
        
    )


ft.app(target=main)