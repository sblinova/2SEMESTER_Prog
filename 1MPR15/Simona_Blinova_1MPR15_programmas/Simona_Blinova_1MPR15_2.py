# Programma, kas veic teksta šifrēšanu un atšifrēšanu izmontojot Morzes kodu
# Programmas autors Simona Bļinova
# Versija 1.0

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

darbiba = input('Ievadiet vēlamo darbību (c - šifrēt, d - atšifrēt) --> ')
print('')

while True:
    if darbiba == 'c':
        print('Ievadiet tekstu ar latīņu alfabēta burtiem bez punktuacijas zīmem!')
        
        teksts = input('Ievadiet šifrējamo tekstu --> ')
        teksts = teksts.upper()
        
        teksta_vardi = teksts.rsplit(' ')
        #print(teksts)
        
        vardi = []
        for i in range(len(teksta_vardi)):
            if teksta_vardi[i] != '':
                vardi.append(teksta_vardi[i])
                
        #print(vardi)
        
        morzes_kods = ''
        for vards in vardi:
            for burts in vards:
                for key, val in morse.items():
                    if burts == key:
                        morzes_kods += val + ' '
            morzes_kods += ' '
            
        print(f'{teksts} --> {morzes_kods}')   
        break
    
    elif darbiba == 'd':
        print('Ievadiet tekstu morzes kodā izmantojot tikai "." un "-" ar 1 atstarpi starp katra vārda burtiem un 2 atstarpēm starp vārdiem.')
        
        morzes_kods = input('Ievadiet tekstu morzes kodā --> ')
        morzes_koda_simboli = morzes_kods.rsplit(' ')
        #print(teksts)
        
        teksts = ''
        for kods in morzes_koda_simboli:
            #print(kods)
            if kods != '':
                for key, val in morse.items():
                    if kods == val:
                        teksts += key  
            else:
                teksts += ' '
                
        print(f'{morzes_kods} --> {teksts}')
        break
        
    else:
        print('Tādas darbības nav!')
        print('Programma beidz darbību.')
        break
    