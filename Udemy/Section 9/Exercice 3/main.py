'''
Jeu du simon:


'''
import os
import time
import random


s = ""
for i in range(4):
    n = random.randint(0,9)
    s += str(n)

while True:
    print(s)
    print("retiens la sequence de nombre")
    seq_user = input("Votre réponse: ")
    if seq_user == s:
        print("Bonne réponse")
    else:
        break
    chaine_alt = random.randint(0,9)
    s += str(chaine_alt)
print("perdu")
