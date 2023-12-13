from tkinter import *
from decimal import *
from tkinter import messagebox


wynik=str('0')    
class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('kalkulator')
        self.geometry("325x375")
        self.resizable(0, 0)

class Przycisk(Button):
    def __init__(self, value, name):
        super().__init__(text=name, padx=20, pady=20, command=self.on_click)
        self.value=value
        self.name=name
    def on_click(self):
        e.insert(END, str(self.value))
      
        
print(wynik)
okno=Window()
e = Entry(width=47, borderwidth=7)
e.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

p1 =Przycisk('1', '1')
p2 =Przycisk('2', '2')
p3 =Przycisk('3', '3')
p4 =Przycisk('4', '4')
p5 =Przycisk('5', '5')
p6 =Przycisk('6', '6')
p7 =Przycisk('7', '7')
p8 =Przycisk('8', '8')
p9 =Przycisk('9', '9')
p0 =Przycisk('0', '0')
dot =Przycisk('.', '.')

p1.grid(column=0, row=2)
p2.grid(column=1, row=2)
p3.grid(column=2, row=2)
p4.grid(column=0, row=3)
p5.grid(column=1, row=3)
p6.grid(column=2, row=3)
p7.grid(column=0, row=4)
p8.grid(column=1, row=4)
p9.grid(column=2, row=4)
p0.grid(column=1, row=5)
dot.grid(column=2, row=5)


add=Przycisk('+', '+')
sub=Przycisk('-', '-')
div=Przycisk('/', '/')
mul=Przycisk('*', '*')
power=Przycisk('**', '^')
sqrt=Przycisk('**(1/', 'x root y')
pc=Przycisk(')', ')')
po=Przycisk('(', '(')

def oblicz():
        global wynik
        if (e.get()).find('/0') != -1:
            messagebox.showerror('Python Error', 'Nie można dzielić przez 0!')
        wynik=round(eval(str(e.get())), 3)
        e.delete(0, END)
        e.insert(END, str(wynik))
        



add.grid(column=5, row=5)
sub.grid(column=5, row=4)
div.grid(column=5, row=2)
mul.grid(column=5, row=3)
power.grid(column=3, row=2)
sqrt.grid(column=0, row=1 , columnspan=2)
pc.grid(column=3, row=4)
po.grid(column=3, row=3)



eq = Button(okno, text="=", padx=20, pady=20,  relief="groove", command=oblicz)
eq.grid(column=3, row=5)
clear = Button(okno, text="clear", padx=45, pady=20,  relief="groove", command=lambda : e.delete(0, END))
clear.grid(column=2, row=1, columnspan=2)
delete= Button(okno, text="<-", padx=20, pady=20,  relief="groove", command=lambda : e.delete(e.index(END)-1, END))
delete.grid(row=1, column=5, columnspan=1)

okno.mainloop()
