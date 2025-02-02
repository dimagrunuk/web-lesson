import os
import flet as ft
from src.ui.screens.login import login_screen
from src.ui.screens.register import register_screen
from src.ui.screens.welcome import welcome_screen

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        if page.route == "/login":
            page.views.append(ft.View("/login", [login_screen(page)]))
        elif page.route == "/register":
            page.views.append(ft.View("/register", [register_screen(page)]))
        elif page.route == "/welcome":
            page.views.append(ft.View("/welcome", [welcome_screen(page)]))
        else:  # Головний екран
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.Text("Ласкаво просимо до Habit Tracker!", size=24),
                        ft.ElevatedButton("Вхід", on_click=lambda e: page.go("/login")),
                        ft.ElevatedButton("Реєстрація", on_click=lambda e: page.go("/register")),
                    ],
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

if __name__ == '__main__':
    # Зчитування порту, який задає Heroku (якщо не задано, використовується 8500)
    port = int(os.environ.get("PORT", 8500))
    ft.app(target=main, port=port, view=ft.FLET_APP)
