#Exercice de pyton n°1
# https://python.developpez.com/cours/apprendre-python-3/?page=exercices-corriges#L14-2-1
# Par gerricane
print("Programme de caclul de volume")
hauteur = float(input("Donne une hauteur:"))
rayon = float(input("Quel est le rayon du cercle:"))
rayonCarre = rayon**2
print(f'le rayon du cercle est de {rayon} et sont carré et de {rayonCarre}')
Pi = 3.14
print(f'Pi vaut {Pi}')
volume = Pi * rayonCarre * hauteur / 3

print(f'le volume du cone est de {volume}')