import random

#powitanie
print("Witaj w świecie wisielca! Podaj swój nick:")
pseudonim = input()

#lista haseł
lista = ['sekret', 'tunczyk', 'brokul', 'kicia', 'James', 'Tarantula']

#hasło
haslo = str(lista[random.randint(0, len(lista)-1)])
tablica = list(haslo)

#tablica służy do wyświetlania _ _ _ _
for i in range(len(haslo)):
    tablica[i] = '_'

#zmienna reprezentująca ilość żyć
zycia = 6

#pętla while, w której będzie realizowana gra
while zycia > 0:
    print('')
    print(pseudonim, 'pozostało Ci ', zycia, 'życ')
    print('')
    print(' '.join(tablica))
    print(' ')

    #prosimy użytownika, aby podał swoją literę
    print('Podaj swoją literę:')
    litera = input()

    #udało się odgadnąć
    if litera in haslo:
        #zmieniamy znak podkreślenia na odgadniętą literę
        for i in range(len(haslo)):
            if(haslo[i] == litera):
                tablica[i] = litera
        #sprawdzamy czy tablica tablica = hasło
        #czy udało się odgadnąć cały wyraz
        if ''.join(map(str, tablica)) == haslo:
            print('')
            print(pseudonim, 'pozostało Ci ', zycia, 'życ')
            print('')
            print(' '.join(tablica))
            print(' ')

            print(pseudonim, "Wygrałeś!")
            break
    #nie udało się odgadnąć
    else:
        zycia -= 1