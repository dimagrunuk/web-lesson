import flet as ft
from src.api.api import login

def login_screen(page):
    def handle_login(e):
        response = login(email_field.value, password_field.value)
        # Припускаємо, що відповідь містить ключ "access_token" та "user_data" з полем "name"
        if "access_token" in response:
            # Зберігаємо ім'я користувача у властивість page.user_name
            page.user_name = response.get("user_data", {}).get("name", "Користувач")
            # Перенаправляємо на сторінку з привітанням
            page.go("/welcome")
        else:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Вхід"),
                content=ft.Text(response.get("message", "Помилка входу")),
                actions=[ft.TextButton("OK", on_click=lambda e: close_dialog(e))]
            )
            page.dialog.open = True
            page.update()

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    def go_back(e):
        page.go("/")  # Повертаємо на головний екран

    email_field = ft.TextField(label="Email")
    password_field = ft.TextField(label="Пароль", password=True)

    login_button = ft.ElevatedButton("Увійти", on_click=handle_login)
    back_button = ft.TextButton("Назад", on_click=go_back)

    return ft.Column([
        email_field,
        password_field,
        login_button,
        back_button
    ])
