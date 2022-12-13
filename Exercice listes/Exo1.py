# Liste Exerices - Demander nom de personnes
# Demander nom de personnes
# Boucle infinie, sort quand le nom est vide
# Seulement a la fin, afficher les noms

nom = []

while True:
    reponse_user = input("Nom de la personne: ")
    if reponse_user == "":
        break
    else:
        nom.append(reponse_user)

for i in range (len(nom)):
    print(f"{i+1}) {nom[i]}")

