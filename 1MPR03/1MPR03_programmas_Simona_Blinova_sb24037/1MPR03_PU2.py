import tkinter as tk
from tkinter import ttk


def izmaina():
    darbibas = ['+', '-', '*', '/']
    darbibas_vertiba = poga1.cget('text')
    # print(darbibas_vertiba)
    kartas_numurs = darbibas.index(darbibas_vertiba)
    # print(kartas_numurs)

    darbibu_skaits = len(darbibas)
    if kartas_numurs == darbibu_skaits - 1:
        kartas_numurs = 0
    else:
        kartas_numurs += 1

    poga1.config(text=f'{darbibas[kartas_numurs]}')


def komandas(e):
    parbaude(e)
    poga()


def parbaude(e):
    objekts = e.widget
    skaitlis = objekts.get()
    if naturals(skaitlis) == 'f':
        kr = 'red'
        poga2.config(state=tk.DISABLED)
    else:
        kr = 'white'
    krasa(objekts, kr)


def krasa(a, b):
    a.config(background=b)


def naturals(a):
    try:
        if a == '':
            raise Exception
        a = int(a)
        if a < 0:
            raise Exception
        else:
            return 't'
    except:
        return 'f'      


def poga():
    if naturals(skaititajs1.get()) == 't' and naturals(saucejs1.get()) == 't' and naturals(skaititajs2.get()) == 't' and naturals(saucejs2.get()) == 't':
        poga2.config(state=tk.NORMAL)
    else:
        poga2.config(state=tk.DISABLED)


def LKD(starp_skaititajs, starp_saucejs):
    if starp_skaititajs > starp_saucejs:
        lielakais_skaitlis = starp_skaititajs
        mazakais_skaitlis = starp_saucejs
    else:
        lielakais_skaitlis = starp_saucejs
        mazakais_skaitlis = starp_skaititajs
    
    while mazakais_skaitlis != 0:
        atlikums = lielakais_skaitlis % mazakais_skaitlis
        lielakais_skaitlis = mazakais_skaitlis
        mazakais_skaitlis = atlikums
    
    return lielakais_skaitlis


def rezultats():
        skaititajs1.configure(background='white')
        saucejs1.configure(background='white')
        skaititajs2.configure(background='white')
        saucejs2.configure(background='white')

        dala1 = []
        dala2 = []

        dala1.append(int(skaititajs1.get()))
        dala1.append(int(saucejs1.get()))
        dala2.append(int(skaititajs2.get()))
        dala2.append(int(saucejs2.get()))

        darbibas_zime = poga1.cget('text')

        match darbibas_zime:
            case '+':
                if dala1[1] == dala2[1]:
                    starp_skaititajs = dala1[0] + dala2[0]
                    starp_saucejs = dala1[1]
                else:
                    starp_saucejs = dala1[1] * dala2[1]
                    starp_skaititajs1 = dala1[0] * dala2[1]
                    starp_skaititajs2 = dala2[0] * dala1[1]
                    starp_skaititajs = starp_skaititajs1 + starp_skaititajs2
            case '-':
                if dala1[1] == dala2[1]:
                    starp_skaititajs = dala1[0] - dala2[0]
                    starp_saucejs = dala1[1]
                else:
                    starp_saucejs = dala1[1] * dala2[1]
                    starp_skaititajs1 = dala1[0] * dala2[1]
                    starp_skaititajs2 = dala2[0] * dala1[1]
                    starp_skaititajs = starp_skaititajs1 - starp_skaititajs2
            case '*':
                starp_skaititajs = dala1[0] * dala2[0]
                starp_saucejs = dala1[1] * dala2[1]
            case '/':
                starp_skaititajs = dala1[0] * dala2[1]
                starp_saucejs = dala1[1] * dala2[0]

        if starp_skaititajs < 0:
            zime.config(text='-')
        else:
            zime.config(text=' ')

        starp_skaititajs = abs(starp_skaititajs)
        starp_saucejs = abs(starp_saucejs)

        dalitajs = LKD(starp_skaititajs, starp_saucejs)

        starp_skaititajs = starp_skaititajs / dalitajs
        starp_saucejs = starp_saucejs / dalitajs

        if starp_saucejs < starp_skaititajs:
            vesela_dala = int(starp_skaititajs // starp_saucejs)
            starp_skaititajs -= vesela_dala * starp_saucejs
        else:
            vesela_dala = ' '

        if starp_skaititajs == 0:
            starp_skaititajs = 1

        veseli.config(text=f'{vesela_dala}')
        skaititajs3.config(text=f'{int(starp_skaititajs)}')
        saucejs3.config(text=f'{int(starp_saucejs)}')


logs = tk.Tk()
logs.geometry('320x110')
logs.title('1MPR03_5 Simona Bļinova')

skaititajs1 = tk.Entry(logs)
skaititajs1.place(x=25, y=25, height=25, width=50)
skaititajs1.bind('<KeyRelease>', komandas)

sadalisanas_linija1 = ttk.Separator(logs, orient='horizontal')
sadalisanas_linija1.place(x=25, y=55, height=2, width=50)

saucejs1 = tk.Entry(logs)
saucejs1.place(x=25, y=60, height=25, width=50)
saucejs1.bind('<KeyRelease>', komandas)

poga1 = tk.Button(logs, text='+', command=izmaina)
poga1.place(x=85, y=45, height=20, width=20)

skaititajs2 = tk.Entry(logs)
skaititajs2.place(x=115, y=25, height=25, width=50)
skaititajs2.bind('<KeyRelease>', komandas)

sadalisanas_linija2 = ttk.Separator(logs, orient='horizontal')
sadalisanas_linija2.place(x=115, y=55, height=2, width=50)

saucejs2 = tk.Entry(logs)
saucejs2.place(x=115, y=60, height=25, width=50)
saucejs2.bind('<KeyRelease>', komandas)

poga2 = tk.Button(logs, text='=', state=tk.DISABLED, command=rezultats)
poga2.place(x=175, y=45, height=20, width=20)

zime = tk.Label(logs, text=' ')
zime.place(x=205, y=50, height=10, width=10)

veseli = tk.Label(logs, text=' ')
veseli.place(x=225, y=50, height=10, width=10)

skaititajs3 = tk.Label(logs, text='...')
skaititajs3.place(x=245, y=25, height=25, width=50)

sadalisanas_linija3 = ttk.Separator(logs, orient='horizontal')
sadalisanas_linija3.place(x=245, y=55, height=2, width=50)

saucejs3 = tk.Label(logs, text='...')
saucejs3.place(x=245, y=60, height=25, width=50)

logs.mainloop()