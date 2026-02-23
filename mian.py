import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto Flet - Estilos de Texto"
    page.bgcolor = ft.Colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto1 = ft.Text(
        "Texto 1 - Título Principal",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_400,
        italic=True
    )

    texto2 = ft.Text(
        "Texto 2 - Subtítulo",
        size=30,
        weight=ft.FontWeight.W_600,
        color=ft.Colors.GREEN_400,
        underline=True
    )

    texto3 = ft.Text(
        "Texto 3 - Texto normal",
        size=20,
        color=ft.Colors.ORANGE_400,
        font_family="Courier New"
    )

    page.add(
        ft.Column(
            [
                texto1,
                texto2,
                texto3
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)