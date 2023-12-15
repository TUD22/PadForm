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
        plik.write(f'imie: {imie.get()}\nnzawisko: {nazwisko.get()}\nwiek: {wiek.get()}\nDoświadczenie: {doswiadczenie.get()}\nPłeć: {plec}')
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
    def __init__(self, text, rozmiar='10'):
        super().__init__(text=text, font=('Arial', rozmiar))

class Radio(Radiobutton):
    def __init__(self, text, value, var):
        self.text=text
        super().__init__(text=text, value=value, command=self.wybor, variable=var)
    def wybor(self):
        global plec
        plec=self.text
        print(plec)

plec =''

okno=Window()
send=Przycisk('Wyślij')
imie=Input()
nazwisko=Input()
doswiadczenie=Input()
scroll=Suwak(1, 20, 'horizontal')
wiek=Licznik(1, 100)
Header=Napis('Formularz do mafii', 25)
Limie=Napis('Imie')
Lnazwisko=Napis('Nazwisko')
Ldoswiadczenie=Napis('Doświadczenie w mafii')
Lwiek=Napis('Wiek')
telefon=Input()
Ltelefon=Napis('Numer telefonu')
pseudonim=Input()
LPseudonim=Napis('Twoje imię w gangu')
Lpraca=Napis('Gdzie teraz pracujesz?')
praca=Input()
m=Radio('Mężczyzna' ,'M', plec)
k=Radio('Kobieta', 'K', plec)



Header.grid(column=1, row=0, columnspan=4)
Limie.grid(column=1, row=1)
imie.grid(column=2, row=1)
Lnazwisko.grid(column=3, row=1)
nazwisko.grid(column=4, row=1)
Lwiek.grid(column=1, row=3)
wiek.grid(column=2, row=3)
Ltelefon.grid(column=3, row=3)
telefon.grid(column=4, row=3)
LPseudonim.grid(column=1, row=4, columnspan=2)
pseudonim.grid(column=3, row=4)
m.grid(column=1, row=5)
k.grid(column=2, row=5)
Lpraca.grid(column=3, row=5)
praca.grid(column=4, row=5)
Ldoswiadczenie.grid(column=1, row=6, columnspan=2)
doswiadczenie.grid(column=3, row=6)

# scroll.grid(column=1, row=5)
send.grid(column=3, row=10)

okno.mainloop()

