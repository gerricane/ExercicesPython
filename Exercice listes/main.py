ma_liste = ["Laurent", "David", "Sébastien", "Jean-François", "Valerie"]

print("Ma liste: ")
print("--- --- --- ---")
for i in range (len(ma_liste)):
    print(ma_liste[i])
print()

reponse = input("Ajouter une nouvelle personne: ")
ma_liste.append(reponse)

print(ma_liste)