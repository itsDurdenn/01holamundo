import flet as ft

def main(page: ft.Page):
    page.title = "App con boton"
    page.bgcolor = "#ce9dff"

    mensaje = ft.Text(
        "Hola mundo.",
        size=30,
        color="#000000",
        weight=ft.FontWeight.BOLD
    )
    page.add(mensaje)
    
if __name__ == "__main__":
    ft.app(target=main)