ma_liste = ["Laurent", "David", "Sébastien", "Jean-François", "Valerie"]

def liste(une_liste, reponse_utilisateur = ""):
    print("Ma liste: ")
    print("--- --- --- ---")
    for i in range(len(une_liste)):
        print(i, une_liste[i])
        if reponse_utilisateur == i:
            print("Entrée deja presente")
            return print("ERREUR")
    une_liste.append(reponse_utilisateur)
    print()


reponse = input("Ajouter une nouvelle personne: ")
liste(ma_liste,reponse)

print("Ici une liste inversée")
for i in ma_liste:
    print(i)