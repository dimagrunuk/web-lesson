import flet as ft
import requests

API_URL = "https://habit-tracker-back-pt2-c5de98999abd.herokuapp.com"

class ProgressChart(ft.Container):
    def __init__(self):
        super().__init__()
        self.chart = ft.BarChart(data=[], width=400, height=300)

        self.load_progress()

    def load_progress(self):
        """Завантаження даних для графіку"""
        response = requests.get(API_URL)
        if response.status_code == 200:
            habits = response.json()
            self.chart.data = [ft.BarChartData(habit["name"], habit["progress"]) for habit in habits]
            self.update()
