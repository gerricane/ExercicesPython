# Exercice 3
# https://python.developpez.com/cours/apprendre-python-3/?page=exercices-corriges#L14-2-3

somme, total, grands = 0, 0, 0

x=int(input("Entre un nombre ou 0 pour quitter: "))
while x > 0:
    somme += x
    total += 1
    if x > 100:
        grands += 1
    x = int (input("x (0 pour terminer)"))
    
print("La somme est de", somme)
print(total, "valeurs en touts et ",grands, " grand nombres")