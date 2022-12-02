'''
Jeu du simon:


'''
import os
import time
import random

def clear_screen():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def compteur(nb):
    s = ""
    compteur = 0
    for i in range(nb):
        n = random.randint(0,9)
        s += str(n)
    return s

nombres = 4
compteur_points = 0
resultat = compteur(nombres)
print(resultat)
reponse = input("Votre réponse: ")
if reponse == resultat:
    print("Bonne réponse")
    compteur_points += 1
    nombres += 1
    resultat = compteur(nombres)
    print(nombres)
else:
    print("perdu")

