import flet as ft
from src.api.api import register

def register_screen(page):
    def handle_register(e):
        response = register(
            email=email_field.value,
            password=password_field.value,
            name=name_field.value,
        )
        dialog = ft.AlertDialog(
            title=ft.Text("Реєстрація"),
            content=ft.Text(response.get("message", "Помилка реєстрації")),
            actions=[ft.TextButton("OK", on_click=lambda e: close_dialog(e))]
        )
        print(f"Запит відправлено. Відповідь сервера: {response}")
        page.dialog = dialog
        page.dialog.open = True
        page.update()

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    def go_back(e):
        page.go("/")  # Повертає на головний екран

    email_field = ft.TextField(label="Email")
    password_field = ft.TextField(label="Пароль", password=True)
    name_field = ft.TextField(label="Ім'я")

    register_button = ft.ElevatedButton("Зареєструватися", on_click=handle_register)
    back_button = ft.TextButton("Назад", on_click=go_back)

    return ft.Column([
        email_field,
        password_field,
        name_field,
        register_button,
        back_button
    ])
