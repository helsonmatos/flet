from flet import *
from flet import colors,icons

# CREATE APPBAR

appmenu = ResponsiveRow([
    Container(
        bgcolor="#AEAEAE",
        padding=10,
        content=Column(
            col=[12,12,12],
            controls=[
                Row([
                    Text("oi"),
                    Text("oi"),
                    Text("oi"),
                    Text("oi"),
                ])
            ]
        )
    )
])
