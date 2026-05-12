import flet as ft

def main(page: ft.Page):
    page.title = "App con botón"

    page.window_width = 320  
    page.window_height = 420
    page.bgcolor = "#ce9dff"
   
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    mensaje2 = ft.Text("Hola Mundo!", size=16)
    page.add(mensaje2)

    mensaje = ft.Text("Hola, escribe algo abajo 👇", size=16)

    caja_texto = ft.TextField(label="Escribe tu mensaje")
    
    caja_texto2 = ft.TextField(label="Escribe algo")
    page.add(caja_texto2)

    def cambiar_texto(e):
        mensaje.value = f"Tú escribiste: {caja_texto.value}"  
        mensaje.color = "purple"   # Cambia el color del texto
        page.update()

    boton1 = ft.Button("Mostrar texto", on_click=cambiar_texto)

    page.add(
        ft.Column(
            controls=[mensaje, caja_texto, boton1],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)