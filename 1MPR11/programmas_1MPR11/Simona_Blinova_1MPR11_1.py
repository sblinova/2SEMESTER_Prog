# Programma, kas veic eksāmena simulāciju pēc uzdevuma nosacījumiem
# Programmas autors Simona Bļinova
# Versija 1.0

import random
import string

studenti = set()
biletes = set()

for i in range(1, 57):
    studenti.add(i)
    
for i in range(65, 91):
    biletes.add(chr(i))
    
#print(studenti)
#print(biletes)

studentu_atbildes = []

for i in range(10):
    while True:
        st = random.randint(1, 56)
        b = random.choice(string.ascii_uppercase)
        #print(st)
        #print(chr(b))
        if b in biletes and st in studenti:
            studenti.remove(st)
            biletes.remove(b)
            break
            
    #print(studenti)
    #print(biletes)
    print(f'Students: {st}, biļete: {b}')
        
    studentu_atbildes.append((st, b))
    
#print(studentu_atbildes)

while len(studenti) > 0:
    #print(studentu_atbildes)
    a = studentu_atbildes[0]
    studentu_atbildes.pop(0)
    
    biletes.add(a[1])
    
    while True:
        st = random.randint(1, 56)
        b = random.choice(string.ascii_uppercase)
        #print(st)
        #print(chr(b))
        if b in biletes and st in studenti:
            studenti.remove(st)
            biletes.remove(b)
            break
        
    print(f'Students: {st}, biļete: {b}')
    studentu_atbildes.append((st, b))

    