# Programma, kas pārbauda vai lietotāja ievadīts sudoku ir pareizi atrisināts
# Programmas autors Simona Bļinova
# Versija 1.3

import numpy
import random

def sudoku():
    c = numpy.empty((9, 9))
    
    for i in range(9):
        for j in range(9):
            a = int(input(f'Ievadiet skaitli {i+1}.rindā {j+1}.kolonnā --> '))
            c[i, j] = a
        
    return c


def izvade(a):
    for i in range(9):
        v = ''
        for j in range(9):
            v += str(round(a[i, j])) + ' '
        print(v)


def parbaude(a):
    if rindas(a) == False:
        return False
    if kolonnas(a) == False:
        return False
    if kvadrati(a) == False:
        return False
    return True

    
def rindas(a):
    for i in range(9):
        b = set()
        for j in range(9):
            b.add(a[i, j])
        if len(b) != 9:
            #print('r')
            #print(i)
            #print(len(b))
            return False
    return True


def kolonnas(a):
    for i in range(9):
        b = set()
        for j in range(9):
            b.add(a[j, i])
        if len(b) != 9:
            #print('k')
            #print(j)
            #print(len(b))
            return False
    return True  


def kvadrati(a):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            b = set()
            for k in range(0+i, 3+i, 1):
                for p in range(0+j, 3+j, 1):
                    b.add(a[k, p])
            if len(b) != 9:
                #print('kv')
                #print(i, j)
                #print(len(b))
                return False
    return True
                    
    
s = sudoku()

print(' ')

izvade(s)

print(' ')

paz = parbaude(s)
#print(paz)

if paz == True:
    print('Sudoku IR atrisināts pareizi.')
else:
    print('Sudoku NAV atrisināts pareizi.')

