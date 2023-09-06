from flet import *
import flet as ft
import appmenu
import section1
import section2

def main(page: Page):

    page.spacing=0,
    page.scroll = "auto",
    page.update()
    page.add(
       appmenu.appmenu,
       section1.section1,
       section2.section2
    )
    
        

ft.app(target=main)