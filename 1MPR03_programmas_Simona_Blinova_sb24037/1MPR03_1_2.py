import tkinter as tk
import math


def mpr1():
    garums_kanva = 600
    x = 0
    y = 0
    kanva.create_rectangle(0, 0, 600, 600, fill='grey')
    kvadrati(x, y, garums_kanva)


def kvadrati(x, y, garums_kanva):
    garums = garums_kanva // 3
    x_balts = x + garums
    y_balts = y + garums
    kanva.create_rectangle(x_balts, y_balts, x_balts + garums, y_balts + garums, fill='white')
    if garums > 20:
        kvadrati(x, y, garums)
        kvadrati(x + garums, y, garums)
        kvadrati(x + garums*2, y, garums)
        kvadrati(x, y + garums, garums)
        kvadrati(x, y + garums*2, garums)
        kvadrati(x + garums, y + garums*2, garums)
        kvadrati(x + garums*2, y + garums, garums)
        kvadrati(x + garums*2, y + garums*2, garums)


def kohazvaigzne(kanva, virsotnex1, virsotney1, virsotnex2, virsotney2, pakape):
    if pakape == 0: # funkcijas pārtraukuma gadījums
        kanva.create_line(virsotnex1, virsotney1, virsotnex2, virsotney2, fill="black")
    else:
        x_garums = virsotnex2 - virsotnex1 # garums starp pēdejo un pirmo punktu
        y_garums = virsotney2 - virsotney1
        # aprēķina nākamos punktus
        x11 = virsotnex1 + x_garums / 3 
        y11 = virsotney1 + y_garums / 3
        x22 = virsotnex1 + 2 * x_garums / 3
        y22 = virsotney1 + 2 * y_garums / 3
        x33 = (virsotnex1 + virsotnex2) / 2 - (virsotney2 - virsotney1)*(math.sqrt(3) / 6)
        y33 = (virsotney1 + virsotney2) / 2 + (virsotnex2 - virsotnex1)*(math.sqrt(3) / 6) 
        # zīmē Koha līkni
        kohazvaigzne(kanva, virsotnex1, virsotney1, x11, y11, pakape - 1)
        kohazvaigzne(kanva, x11, y11, x33, y33, pakape - 1)
        kohazvaigzne(kanva, x33, y33, x22, y22, pakape - 1)
        kohazvaigzne(kanva, x22, y22, virsotnex2, virsotney2, pakape - 1)


def mpr2():
    virsotne_x1 = 300
    virsotne_y1 = 100
    virsotne_x2 = 150
    virsotne_y2 = 400
    virsotne_x3 = 450
    virsotne_y3 = 400
    kohazvaigzne(kanva, virsotne_x2, virsotne_y2, virsotne_x3, virsotne_y3, 4)
    kohazvaigzne(kanva, virsotne_x3, virsotne_y3, virsotne_x1, virsotne_y1, 4)
    kohazvaigzne(kanva, virsotne_x1, virsotne_y1, virsotne_x2, virsotne_y2, 4)


def notirit():
    kanva.delete('all')


logs = tk.Tk()
logs.geometry('825x650')
logs.title('1MPR02 Simona Bļinova')

kanva = tk.Canvas(logs, background='white')
kanva.place(x=200, y=25, height=600, width=600)

b1 = tk.Button(logs, text='1MPR03_1', command=mpr1)
b1.place(x=25, y=50, height=25, width=150)

b2 = tk.Button(logs, text='1MPR03_2', command=mpr2)
b2.place(x=25, y=85, height=25, width=150)

bnotirit = tk.Button(logs, text='Notīrīt', command=notirit)
bnotirit.place(x=25, y=120, height=25, width=150)

logs.mainloop()