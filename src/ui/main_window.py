import flet as ft
import requests

API_URL = "https://habit-tracker-back-pt2-c5de98999abd.herokuapp.com"

def main(page: ft.Page):
    page.title = "Habit Tracker"
    page.window_width = 500
    page.window_height = 600

    habits_list = ft.Column()

    def load_habits(e=None):
        habits_list.controls.clear()
        response = requests.get(f"{API_URL}/habit")
        if response.status_code == 200:
            habits = response.json()
            for habit in habits:
                habits_list.controls.append(ft.Text(f"{habit['name']} - {habit['frequency']}"))
        page.update()

    from src.ui.screens.habit_form import AddHabitDialog
    add_habit_dialog = AddHabitDialog(page, refresh_callback=load_habits)

    def open_add_habit_dialog(e):
        page.dialog = add_habit_dialog
        page.dialog.open = True
        page.update()

    add_button = ft.ElevatedButton("Додати звичку", on_click=open_add_habit_dialog)
    refresh_button = ft.ElevatedButton("Оновити список", on_click=load_habits)

    page.add(ft.Column([add_button, refresh_button, habits_list]))

ft.app(target=main)
