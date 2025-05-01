# Programma, kas reālize 4 spēlētāju karšu izvadi.
# Programmas autors Simona Bļinova
# Versija 1.0

import random

k = set()

for i in range(4):
    kartis = f'{i+1}.spēlētāja kartis: '
    for j in range(6):
        while True:
            # 52 kartis --> 0 - 51
            x = random.randint(0, 51)
            if not x in k:
                k.add(x)
                ks = x // 13
                ksk = x % 13
                
                match ksk:
                    case 9:
                        kartis += chr(9824+ks)+'J '
                    case 10:
                        kartis += chr(9824+ks)+'Q '
                    case 11:
                        kartis += chr(9824+ks)+'K '
                    case 12:
                        kartis += chr(9824+ks)+'A '
                    case _:
                        kartis += chr(9824+ks)+str(ksk+2)+' '
                        
                break
            
    print(kartis)
