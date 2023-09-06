from flet import *

def main(page:Page):
    page.title = "NavRail"
    
    rail = NavigationRail(
        #extended=True,
        selected_index=0,
        bgcolor= colors.CYAN_100,
        min_width= 120,
        min_extended_width= 200,
        label_type= NavigationRailLabelType.ALL,
        group_alignment=-0.8,
        leading= FloatingActionButton(icon=icons.CREATE, text="Criar",),
        destinations=[
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, label="Favorito"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.BOOKMARK_BORDER),
                selected_icon_content=Icon(icons.BOOKMARK),
                label="Marcar"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.SETTINGS_OUTLINED),
                selected_icon_content=Icon(icons.SETTINGS),
                label="Definições"
            )
        ],
        on_change= lambda e: print("Pagina selecionada:", e.control.selected_index)
    )

    page.add(
        Row(
        [
            rail,
            VerticalDivider(width=5),
            Column([Text("corpo")]),
            
        ],
        alignment=MainAxisAlignment.START,
        expand=True
        )
    )



app(target=main)