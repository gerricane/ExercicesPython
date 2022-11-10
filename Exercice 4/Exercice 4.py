# Exercice 4
# https://python.developpez.com/cours/apprendre-python-3/?page=exercices-corriges#L14-2-4

x = int(input("entrez un nombre entier:"))
while x <1:
    x = int(input("entrez un nombre entier:"))

if x%2 == 0:
    print(x, "est pair")
else :
    print(x, "est impair")