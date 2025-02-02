import flet as ft
from src.api.api import add_habit

class AddHabitDialog(ft.AlertDialog):
    def __init__(self, page, refresh_callback):
        super().__init__()
        self.page = page
        self.refresh_callback = refresh_callback
        self.open = False

        self.name_field = ft.TextField(label="Назва звички")
        self.freq_field = ft.Dropdown(
            label="Частота",
            options=[
                ft.dropdown.Option("Daily"),
                ft.dropdown.Option("Weekly"),
                ft.dropdown.Option("Monthly"),
            ]
        )

        add_button = ft.ElevatedButton("Додати", on_click=self.add_habit)
        self.content = ft.Column([self.name_field, self.freq_field, add_button])

    def add_habit(self, e):
        name = self.name_field.value
        frequency = self.freq_field.value
        if name and frequency:
           result = add_habit(name, frequency)
           if result:
               self.refresh_callback()
               self.open = False
               self.page.update()
