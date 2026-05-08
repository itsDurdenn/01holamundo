import flet as ft  

def main(page: ft.Page):    
    page.title = "Mi primera app Flet"

    page.bgcolor = "#7CFFE9"  # color del fondo en tono claro

    page.add(
        ft.Text(
            "Hola, mundo desde Flet!", # Enseguida las propiedades para el estilo del texto
            color="#000000", # color del texto un tono gris-azulado
            size=30,           # tamaño de la letra
            weight=ft.FontWeight.BOLD   # weight grosor / ft.FontWeight.BOLD indica negritas
            ),
        ft.Text(
            "BAZINGA!", # Enseguida las propiedades para el estilo del texto
            color="#2F00FF", # color del texto un tono gris-azulado
            size=30,           # tamaño de la letra
            weight=ft.FontWeight.BOLD   # weight grosor / ft.FontWeight.BOLD indica negritas
            )
        )

ft.app(target=main)