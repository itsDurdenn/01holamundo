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

    def cambiar_texto(e):
        mensaje.value = "Has hecho clic en el botón"
        mensaje.color = "#ff0000"
        page.update()

    boton1 = ft.Button("Haz clic aquí", on_click=cambiar_texto)

    tarjeta = ft.Container(
        content=ft.Column(
            controls=[
                mensaje,
                boton1
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        width=400,
        height=300,
        padding=20,
        border_radius=15,
        bgcolor=ft.Colors.GREY_100,
        shadow=ft.BoxShadow(
            blur_radius=10, spread_radius=1, color=ft.Colors.BLACK26
        )
    )
    page.add(
        ft.Column(
            controls=[tarjeta],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)