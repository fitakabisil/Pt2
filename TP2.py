import time
import random
refaire = y #la variable est déja défini comme true (y) audébut du code.
while refaire = y: #si la variable refaire est true (y), le jeu va commencer.
    nombre_essai = 1 #la variable est défini par 1 pour ne pas avoir de message 'tu a réussi avec 0 essais!'.
    prénom = input('Quel est ton prénom?')
    print('bonjour', prénom,'veux-tu jouer à un petit jeu? Bien sûr que oui!')
    time.sleep(1)
    born_minimal = input('Quel est la born minimal?')
    born_maximal = input('Quel est la born maximal?')
    print('je vais choisir un nombre entre', born_minimal,'et',born_maximal)
    value = random.randint(int(born_minimal), int(born_maximal)) #un nombre aléatoire va ête choisie entre les deux limites (les bornes sont transformer en integer).
    while True: # dans cette boucle, l'utilisateur doit trouver le nombre aléatoire.
        essai = int(input('quel est ton essai?')) #la variable d,essai est transformer en integer.
        if value == essai: #cette boucle va être activer si le la variable essai est égale au nombre mistère.
            print("bravo, tu as réussi avec", nombre_essai, "essais!")
            refaire = input("veux-tu réessayer? y ou n?")
            if refaire == ('n'): #ce code va transformé la valeur de la varable en false (n) et met fin au jeu.
                print('meci de jouer.')
                break
         else:
            continue #essentiellement, ce code va recommencer le jeu.
     else: #cette boucle va augmenter la valeur du nombre d'éssai si l'utilisateur devine faut.
            print('essai encore.')
            nombre_essai = nombre_essai + 1
