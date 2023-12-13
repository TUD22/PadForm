from tkinter import *
from tkinter import messagebox

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('Formularz mafia')
        self.geometry("500x600")
        self.resizable(0, 0)

class Przycisk(Button):
    def __init__(self, name):
        super().__init__(text=name, padx=20, pady=20)
        self.name=name

class Input(Entry):
     def __init__(self):
        super().__init__()

class Scroll(Scrollbar):
     def __init__(self):
        super().__init__()
        
okno=Window()
send=Przycisk('wyślij')
imie=Input()
scroll=Scroll()

scroll.set(1, 30)

imie.grid(column=1, row=2)
send.grid(column=1, row=1)
scroll.grid(column=1, row=3)

okno.mainloop()