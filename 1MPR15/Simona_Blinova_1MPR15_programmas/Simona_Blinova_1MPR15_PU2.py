# Programma, kas veic teksta šifrēšanu izmontojot Morzes kodu ar gaismas signālu
# Programmas autors Simona Bļinova
# Versija 1.0

import tkinter
import time

def sifrs():
    morse = {'A': '.-',
         'B': '-...',
         'C': '-.-.',
         'D': '-..',
         'E': '.',
         'F': '..-.',
         'G': '--.',
         'H': '....',
         'I': '..',
         'J': '.---',
         'K': '-.-',
         'L': '.-..',
         'M': '--',
         'N': '-.',
         'O': '---',
         'P': '.--.',
         'Q': '--.-',
         'R': '.-.',
         'S': '...',
         'T': '-',
         'U': '..-',
         'V': '...-',
         'W': '.--',
         'X': '-..-',
         'Y': '-.--',
         'Z': '--..',
         '0': '-----',
         '1': '.----',
         '2': '..---',
         '3': '...--',
         '4': '....-',
         '5': '.....',
         '6': '-....',
         '7': '--...',
         '8': '---..',
         '9': '----.'}
    
    teksts = e.get()
    #print(teksts)
    teksts = teksts.upper()
    
    teksta_vardi = teksts.rsplit(' ')
    #print(teksta_vardi)
    
    vardi = []
    for i in range(len(teksta_vardi)):
        if teksta_vardi[i] != '':
            vardi.append(teksta_vardi[i])
            
    #print(vardi)
    
    morzes_kods = ''
    for vards in vardi:
        #print(vards)
        for burts in vards:
            #print(burts)
            for key, val in morse.items():
                if burts == key:
                    morzes_kods += val + ' '
        morzes_kods += ' '
    
    #print(morzes_kods)
    
    # ērtībai visi izpildes laiki tika sadalīti ar 2
    for i in range(1, len(morzes_kods)):
        if morzes_kods[i] == ' ' and morzes_kods[i-1] == ' ':
            time.sleep(3)
        elif morzes_kods[i-1] == ' ':
            time.sleep(1)
        else:
            if morzes_kods[i-1] == '.':
                #print('1')
                canva.itemconfig(lamp, fill='red')
                canva.update()
                time.sleep(0.5)
                canva.itemconfig(lamp, fill='grey')
                canva.update()
            elif morzes_kods[i-1] == '-':
                #print('2')
                canva.itemconfig(lamp, fill='red')
                canva.update()
                time.sleep(1.5)
                canva.itemconfig(lamp, fill='grey')
                canva.update()
        time.sleep(0.5)

logs = tkinter.Tk()
logs.title('Morzes kods')
logs.geometry('300x300')

canva = tkinter.Canvas(logs, height=100, width=100)
canva.place(x=100, y=150)

lamp = canva.create_oval(10, 10, 90, 90, fill='grey')

l1 = tkinter.Label(logs, text='MORZES KODS')
l1.place(x=100, y=25, height=25, width=100)

l2 = tkinter.Label(logs, text='Ievadiet šifrējamo tekstu:')
l2.place(x=50, y=50, height=25, width=200)

e = tkinter.Entry(logs)
e.place(x=75, y=75, height=25, width=150)

b = tkinter.Button(logs, text='šifrēt', command=sifrs)
b.place(x=125, y=100, height=25, width=50)

logs.mainloop()