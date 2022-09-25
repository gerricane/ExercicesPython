#Exercice n°2 
#https://python.developpez.com/cours/apprendre-python-3/?page=exercices-corriges#L14-2-2
 
prixHT = float(input("Entrez un prix hors taxe: "))
prixTTC = prixHT * (1 + 0.20)
print(f'Le prix TTC et de {prixTTC}€')