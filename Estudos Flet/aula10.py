from flet import *


def main(page: Page):
    page.title = "AppBARRR"
    page.appbar = AppBar(
        leading = Icon(icons.ADD),
        leading_width = 80,
        bgcolor ="#003377",
        title = Text("Minha loja", color="white"),
        center_title = True,
        actions = [
            IconButton(icons.WB_SUNNY_OUTLINED),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text= "login"),
                    PopupMenuItem(),
                    PopupMenuItem(text= "conta"),
                    PopupMenuItem(),
                    PopupMenuItem(text= "notificações"),
                    PopupMenuItem(),
                    PopupMenuItem(text= "informações"),
                    PopupMenuItem(),
                    PopupMenuItem(text= "exit")
                ]
            )
        ]
    )
    
    
    
    page.add(Text("corpo!"))


app(target=main)