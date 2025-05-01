# Programma, kas reālize teātra biļešu iegādi
# Programmas autors Simona Bļinova
# Versija 1.3

import numpy
import math
import random

def zale(a, b):
    c = numpy.empty((a, b+1))
    for i in range(a):
        c[i,0] = i+1
        for j in range(b):
            c[i, j+1] = j+1
    c = numpy.array(c, dtype='i')
    return c


def aiznemts(a):
    n = a.shape[0]
    m = a.shape[1]
    vs = n * (m-1)
    avs = math.floor(vs * 0.5)
    #print(avs)
    while avs >= 0:
        randn = random.randint(1, n)
        randm = random.randint(1, m-1)
        a[randn-1, randm] = 0
        avs -= 1
    return a


def izvade(a):
    n = a.shape[0]
    m = a.shape[1]
    
    if len(str(n)) >= len(str(m-1)):
        garums = len(str(n))
    else:
        garums = len(str(m-1))
        
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
                
            if j == 0:
                rinda += '| '
            else:
                rinda += ' '
                
        print(rinda)
    

rindas = int(input('Ievadiet rindu skaitu teātrī --> '))
vietas = int(input('Ievadiet vietu skaitu rindā --> '))
print(' ')
        
zale = zale(rindas, vietas)
zale = aiznemts(zale)
#izvade(zale)

print('Sedvietu iegāde')
print(' ')

izpardots = numpy.empty((rindas, vietas+1))
for i in range(rindas):
    izpardots[i, 0] = i+1
    for j in range(vietas):
        izpardots[i, j+1] = 0
    izpardots = numpy.array(izpardots, dtype='i')
#izvade(izpardots)

paz = True
while paz:
    if (zale == izpardots).all():
        print('Biļetes ir izpārdotas!')
        paz = False
    else:
        rinda = int(input('Ievadiet rindu --> '))
        vieta = int(input('Ievadiet vietas numuru --> '))
        
        if rinda > zale.shape[0] or vieta > zale.shape[1]-1:
            print('Tādas sedvietas nav!')
            izvade(zale)
        else:
            if rinda == 0 and vieta == 0:
                paz = False
            else:
                if zale[rinda-1, vieta] == 0:
                    print('Šī vieta ir aizņemta!')
                    izvade(zale)
                else:
                    zale[rinda-1, vieta] = 0
            
#izvade(zale)
        