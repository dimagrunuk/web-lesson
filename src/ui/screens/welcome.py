import flet as ft

def welcome_screen(page: ft.Page):
    # Якщо page.user_name не задано, використаємо значення за замовчуванням
    user_name = getattr(page, "user_name", "Користувачу")
    greeting = f"Вітаємо, {user_name}!"
    return ft.Column([
        ft.Text(greeting, size=24)
    ])
