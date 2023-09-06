import flet as ft


def main(page: ft.Page):
    
    def tecla(e: ft.KeyboardEvent):
        page.add(ft.Text(f"Tecla pressionada: {e.key}, Shift{e.shift}"))
    
    page.on_keyboard_event = tecla

    page.add(ft.Text("Pressione qualquer tecla..."))
    

ft.app(target=main)