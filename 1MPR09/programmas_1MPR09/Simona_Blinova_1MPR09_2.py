# Programma, kas veic labirinta izveidi un un apstaigāšanu
# Programmas autors Simona Bļinova
# Versija 1.2

import numpy
import random
import math

def parbaude(a, b, c):
    try:
        a = int(a)
        if a < 1 or a > b*c:
            raise Exception
        else:
            return int(a)
    except:
        print('Nepareiza vērtība. Programma beidz darbību!')
        exit()

def labirinta_izveide1(a, b):
    c = numpy.empty((a, b))
    for i in range(a):
        for j in range(b):
            sk = input('Ievadiet labirinta '+str(i+1)+'.rindas '+str(j+1)+'.kolonnas skaitli --> ')
            sk = parbaude(sk, a, b)
            c[i, j] = sk
    c = numpy.array(c, dtype='i')
    return c


def labirinta_izveide2(a, b):
    c = numpy.empty((a, b))
    for i in range(a):
        for j in range(b):
            c[i, j] = random.randint(1, a*b)
    c = numpy.array(c, dtype='i')
    return c   


def skersli(a):
    n = a.shape[0]
    m = a.shape[1]
    vs = n * m
    avs = round(vs * 0.05)
    #print(avs)
    while avs > 0:
        randn = random.randint(1, n)
        randm = random.randint(1, m-1)
        a[randn-1, randm] = 0
        avs -= 1
    return a


def cels(a, b, l, m):
    n1 = l.shape[0]-1
    n2 = l.shape[1]-1
    if a == n1 and b == n2:
        return True
    else:
        ircels = False
        if a < n1 and l[a+1, b] >= l[a, b]:
            m[a+b] = 'uz leju'
            ircels = cels(a+1, b, l, m)
        if not ircels and b < n2 and l[a, b+1] >= l[a, b]:
            m[a+b] = 'pa labi'
            ircels = cels(a, b+1, l, m)
        return ircels
    

def izvade(a):
    n = a.shape[0]
    m = a.shape[1]
    
    garums = len(str(n*m))
        
    for i in range(n):
        rinda = ''
        for j in range(m):
            b = str(a[i, j])
            c = garums - len(b)
            
            if c != 0:
                rinda += ' '*c
                
            if b == '0':
                rinda += 'X'
            else:
                rinda += b
                
            rinda += ' '
                
        print(rinda)    


n = int(input('Ievadiet labirinta rindu skaitu --> '))
m = int(input('Ievadiet labirinta kolonnu skaitu --> '))

labirints = labirinta_izveide1(n, m)
labirints = skersli(labirints)
izvade(labirints)

garums_cels = n + m - 2
marsruts = numpy.empty(garums_cels, 'O')

if cels(0, 0, labirints, marsruts):
    print('Labirintu var iziet virzoties', marsruts)
else:
    print('Labirints nav izejams!')

