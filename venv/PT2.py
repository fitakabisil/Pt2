import time
import random
refaire = y
while refaire = y:
    nombre_essai = 1
    prénom = input('Quel est ton prénom?')
    print('bonjour', prénom,'veux-tu jouer à un petit jeu? Bien sûr que oui!')
    time.sleep(1)
    born_minimal = input('Quel est la born minimal?')
    born_maximal = input('Quel est la born maximal?')
    print('je vais choisir un nombre entre', born_minimal,'et',born_maximal)
    value = random.randint(int(born_minimal), int(born_maximal))
    while True:
        essai = int(input('quel est ton essai?'))
        if value == essai:
            print("bravo, tu as réussi avec", nombre_essai, "essais!")
            refaire = input("veux-tu réessayer? y ou n?")
            if refaire == ('n'):
                print('meci de jouer.')
                break
         else:
            continue
     else:
            print('essai encore.')
            nombre_essai = nombre_essai + 1