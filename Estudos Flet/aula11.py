from flet import *


def main(page: Page):
    page.title = "Rotas"

    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.HOME, label="home"),
            NavigationDestination(icon=icons.EXPLORE, label="explorar"),
            NavigationDestination(icon=icons.GPS_FIXED, label="gps"),
        ]
    )

    page.add(
        Text("corpo do texto"),
        ElevatedButton(text="Clique aqui"))

app(target=main)