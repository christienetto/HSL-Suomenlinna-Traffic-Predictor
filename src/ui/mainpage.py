from tkinter import ttk, StringVar, Canvas, Scrollbar
from tkcalendar import Calendar
import datetime

class MainPage:

    def __init__(self, root, resultpage_view):
        self._root = root
        self.resultpage_view = resultpage_view
        
        self.start()

    def start(self):
        canvas = Canvas(self._root)
        scrollbar = Scrollbar(self._root, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        heading = ttk.Label(scrollable_frame, text="Suomenlinna Ferry Traffic Predictor", font=("Helvetica", 26))
        heading.grid(row=0, column=0, padx=5, pady=50)

        direction = ttk.Label(scrollable_frame, text="Direction", font=("Helvetica", 16))
        direction.grid(row=1, column=0, padx=5, pady=10)

        direction_options = ['To Suomenlinna', 'From Suomenlinna']
        self.dir_var = StringVar(self._root)
        direction_menu = ttk.Combobox(scrollable_frame, textvariable=self.dir_var, values=direction_options, width=20)
        direction_menu['values'] = direction_options
        direction_menu.grid(row=2, column=0, pady=10) 
        direction_menu.current(0)

        date = ttk.Label(scrollable_frame, text="Date", font=("Helvetica", 16))
        date.grid(row=3, column=0, padx=5, pady=10)

        self.cal = Calendar(scrollable_frame, mindate=datetime.date.today(), maxdate=datetime.date(2026, 1, 1))
        self.cal.grid(row=4, column=0, padx=370, pady=10, sticky="nsew")

        time = ttk.Label(scrollable_frame, text="Time (full hour)", font=("Helvetica", 16))
        time.grid(row=5, column=0, padx=5, pady=10)

        self.hour_var = StringVar(value='0')
        hours = [str(hour) for hour in range(24) if hour not in (3, 4, 5)]
        hour_spinbox = ttk.Spinbox(scrollable_frame, values=hours, textvariable=self.hour_var, wrap=True, width=10)
        hour_spinbox.grid(row=6, column=0, padx=5, pady=10)

        weather = ttk.Label(scrollable_frame, text="Expected weather", font=("Helvetica", 16))
        weather.grid(row=7, column=0, padx=5, pady=10)

        temp = ttk.Label(scrollable_frame, text="1. Temperature", font=("Helvetica", 12))
        temp.grid(row=8, column=0, padx=5, pady=10)

        temp_options = ["21 to 30 degrees", "11 to 20 degrees", "1 to 10 degrees", "0 to -9 degrees", "-10 to -19 degrees", "-20 to -30 degrees"]
        self.temp_var = StringVar(self._root)
        temp_menu = ttk.Combobox(scrollable_frame, textvariable=self.temp_var, values=temp_options, width=20)
        temp_menu.grid(row=9, column=0, pady=10)
        temp_menu.current(0)

        wind = ttk.Label(scrollable_frame, text="2. Wind", font=("Helvetica", 12))
        wind.grid(row=10, column=0, padx=5, pady=10)

        wind_options = ["light wind", "moderate wind", "heavy wind"]
        self.wind_var = StringVar(self._root)
        wind_menu = ttk.Combobox(scrollable_frame, textvariable=self.wind_var, values=wind_options, width=20)
        wind_menu.grid(row=11, column=0, pady=10)
        wind_menu.current(0)

        rain = ttk.Label(scrollable_frame, text="3. Precipitation", font=("Helvetica", 12))
        rain.grid(row=12, column=0, padx=5, pady=10)

        rain_options = ["no rain/snow", "light rain", "moderate rain", "heavy rain", "light snow", "moderate snow", "heavy snow"]
        self.rain_var = StringVar(self._root)
        rain_menu = ttk.Combobox(scrollable_frame, textvariable=self.rain_var, values=rain_options, width=20)
        rain_menu.grid(row=13, column=0, pady=10)
        rain_menu.current(0)

        save_button = ttk.Button(scrollable_frame, command=self.handle_prediction, text="Predict the traffic")
        save_button.grid(row=14, column=0, padx=5, pady=50)

        scrollable_frame.columnconfigure(0, weight=1)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def handle_prediction(self):
        direction = self.dir_var.get()
        date = self.cal.get_date()
        time = self.hour_var.get()
        temperature = self.temp_var.get()
        wind = self.wind_var.get()
        precipitation = self.rain_var.get()
        self.resultpage_view(direction, date, time, temperature, wind, precipitation)
