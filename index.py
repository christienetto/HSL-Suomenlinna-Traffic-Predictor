from tkinter import Tk
from src.ui.ui import UI

def main():
    root = Tk()
    root.title("Suomenlinna Ferry Traffic Predictor")
    root.geometry("1000x1000")
    UI(root)

    root.mainloop()

if __name__ == "__main__":
    main()