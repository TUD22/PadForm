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
        super().__init__(text=name, padx=20, pady=20, command=self.send)
    def send(self):
        plik =open('formularz.txt', 'w')
        plik.write(f'imie: {imie.get()}\nnzawisko: {nazwisko.get()}\nwiek: {wiek.get()}\nDoświadczenie: {doswiadczenie.get()}')
        plik.close()

class Input(Entry):
     def __init__(self):
        super().__init__()

class Suwak(Scale):
     def __init__(self, od, do, orient):
        super().__init__(to=do, from_=od, orient=orient)

class Licznik(Spinbox):
     def __init__(self, od, do):
        super().__init__(to=do, from_=od)

class Napis(Label):
    def __init__(self, text, rozmiar):
        super().__init__(text=text, font=('Arial', rozmiar))

okno=Window()
send=Przycisk('wyślij')
imie=Input()
nazwisko=Input()
doswiadczenie=Input()
scroll=Suwak(1, 20, 'horizontal')
wiek=Licznik(1, 100)
Header=Napis('Formularz do mafii', 25)
Limie=Napis('imie', 10)
Lnazwisko=Napis('nazwisko', 10)
Ldoswiadczenie=Napis('Doświadczenie w mafii', 10)
Lwiek=Napis('wiek', 10)


Header.grid(column=1, row=0, columnspan=3)
Limie.grid(column=1, row=1)
Lnazwisko.grid(column=1, row=2)
Ldoswiadczenie.grid(column=1, row=3)
Lwiek.grid(column=1, row=4)
imie.grid(column=2, row=1)
nazwisko.grid(column=2, row=2)
doswiadczenie.grid(column=2, row=3)
scroll.grid(column=1, row=5)
wiek.grid(column=2, row=4)
send.grid(column=5, row=3)

okno.mainloop()

