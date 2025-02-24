# Datne ar visām noderīgām funkcijām
# Programmas autors Simona Bļinova

# Funkcija pārbaudei, lai skaitlis būtu naturāls skaitlis
def naturals_skaitlis(a):
    # meģinājumu skaita skaitītājs (3 meģinājumi ierakstam)
    meginajumi = 1
    while meginajumi <= 3:
        try:
            a = int(a)
            if a > 0:
                return int(a)
            else:
                raise Exception
        except:
            if meginajumi < 3:
                meginajumi += 1
                a = input('Ievadiet naturālo skaitli vēlreiz --> ')
            else:
                print('Programma beidz darbību!')
                exit()


# Funkcija pārbaudei, lai skaitlis būtu vesels skaitlis
def vesels_skaitlis(a):
    # meģinajumu skaitītājs (3 meģinājumi pareizi ievadīt)
    meginajumi = 1
    while meginajumi <= 3:
        try:
            a = int(a)
            return int(a)
        except:
            if meginajumi < 3:
                meginajumi += 1
                a = input('Ievadiet veselo skaitli vēlreiz --> ')
            else:
                print('Programma beidz darbību!')
                exit()


# Funkcijas kombinācijas vērtības aprēķinam
def kombinacija(n, m):
    if n == 0 and m == 0:
        kombinacijas_vertiba = 1
    else:
        n_faktorials = faktorials(n)
        m_faktorials = faktorials(m)
        n_m_starpiba = n - m
        n_m_faktorials = faktorials(n_m_starpiba)
        kombinacijas_vertiba = n_faktorials / (m_faktorials * n_m_faktorials)
    return kombinacijas_vertiba


# Funkcija faktoriāla aprēķinam
def faktorials(a):
    faktoriala_vertiba = 1
    for i in range(1, a+1):
        faktoriala_vertiba *= i
    return faktoriala_vertiba


# Funkcija nuļļu pievienošanai
def nulles(a, p):
    datuma_vertiba = str(a)
    vertibas_garums = len(datuma_vertiba)
    if p == 'g':
        atlikums = 4 - vertibas_garums
    elif p == 'm' or p == 'd':
        atlikums = 2 - vertibas_garums
    datuma_vertiba = '0' * atlikums + datuma_vertiba
    return datuma_vertiba


# Funkcija pārbaudei vai skaitlis ir pirmskaitlis
def vai_pirmskaitlis(a):
    if a < 2:
        return False

    for i in range(2, a//2):
        if a % i == 0:
            return False
    else:
        return True