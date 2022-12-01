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

s = ""
compteur = 0
for i in range(4):
    n = random.randint(0,9)
    s += str(n)

print(s)
time.sleep(5)
clear_screen()

reponse = str(input("Votre réponse: "))
if reponse == s:
    print("Bonne réponse")
    compteur += 1
    print(f"Vous avez {compteur} points")
else:
    print(f"Le nombre etait: {s}")

