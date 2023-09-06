""" Flet Animations Buttons"""

# imports
from flet import (
    flet, Page, UserControl, Column, Card,
    Container, Row, alignment, colors, animation,
    border, Text, transform, IconButton, icons, Scale
    )


import time

global SendState
SendState = True


def main(page: Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    texto = Text(
        "SEND!",
        color=colors.WHITE,
        size=14,
        weight="w700",
        offset= transform.Offset(0,0),
        animate_offset=animation.Animation(duration=900, curve="decelerate"),
        animate_opacity=200,

    )

    botao = IconButton(
        icon=icons.SEND_SHARP,
        icon_color="white",
        icon_size=16,
        offset= transform.Offset(0,0),
        animate_offset=animation.Animation(duration=900, curve="decelerate"),
        rotate=transform.Rotate(11,alignment=alignment.center),
        animate_rotation=animation.Animation(duration=600, curve="decelerate"),
        scale=Scale(scale=1),
        animate_scale=animation.Animation(duration=600, curve="bounceOut"),
        
        
    )

    MainContainer = Container(
        width=140,
        height=45,
        on_hover=lambda e: send_button(e),
        bgcolor=colors.BLUE_700,
        border_radius=10,
        content=Row(
            controls=[
                botao,
                texto,
            ]
        )
    )

    def send_button(e):
        
        if e.data == 'true':
            
            SendState = True
            
            botao.rotate.angle += 1.5
            botao.offset = transform.Offset(0.5,0)
            botao.scale = transform.Scale(1.25)
            botao.update()

            #Texto
            texto.offset = transform.Offset(1,0)
            texto.opacity = 0
            texto.update()
            
        else:
            
            SendState = False

            botao.rotate.angle -= 1.5
            botao.offset = transform.Offset(0,0)
            botao.scale = transform.Scale(1)
            botao.update()

            #Texto
            texto.offset = transform.Offset(0,0)
            texto.opacity = 100
            texto.update()
        
        while SendState == True:
            botao.offset = transform.Offset(0.5,0.09)
            botao.update()
            time.sleep(0.9)
            
            if SendState == False:
                botao.offset = transform.Offset(0.5,0.09)
                botao.update()
                break
            botao.offset = transform.Offset(0.5,-0.09)
            botao.update()
            time.sleep(0.9)

            if SendState == False:
                botao.offset = transform.Offset(0,0)
                botao.update()
                break






    page.add(MainContainer)


flet.app(target=main)