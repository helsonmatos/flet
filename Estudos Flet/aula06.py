import flet as ft

def main(page:ft.Page):
    
    page.title = "App top"
    page.theme_mode = ft.ThemeMode.DARK
    page.update()
    

ft.app(target=main)