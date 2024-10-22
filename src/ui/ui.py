from tkinter import Tk
from src.ui.mainpage import MainPage
from src.ui.resultpage import ResultPage

class UI:

    def __init__(self,root):    
        self._root = root
        self._window = None
        self.mainpage_view()

    def hide_current_view(self):
        if self._window:
            self._root.destroy()
            self._root = Tk()
            self._root.title("Suomenlinna Ferry Traffic Predictor")
            self._root.geometry("1000x1000")
            self._window = None

    def mainpage_view(self):
        self.hide_current_view()
        self._window = MainPage(self._root, self.resultpage_view)

    def resultpage_view(self, direction, date, time, temperature, wind, precipitation):
        self.hide_current_view()
        self._window = ResultPage(self._root, self.mainpage_view, direction, date, time, temperature, wind, precipitation)
