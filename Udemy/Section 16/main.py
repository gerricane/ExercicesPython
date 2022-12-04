def afficher(collection, ecart = 1):
    nb_pizzas = len(collection)
    if nb_pizzas == 0:
        print("---- Aucune Pizza ---")
    else:
        print(f" ---- LISTE DES PIZZAS ({nb_pizzas}) ----")
        for i in collection[:ecart]:
            print(i)
        print()
        print(f"Premiere pizza: {collection[0]}")
        print(f"Derniere pizza: {collection[-1]}")


def pizza_existe(collection,pizza_utilisateur):
    for i in collection:
        if i == pizza_utilisateur:
            return True
    return False

def ajouter_pizza_utilisateur(collection):
    pizza_utilisateur = input("Quelle est la pizza de votre choix ? ")
    if pizza_existe(collection,pizza_utilisateur):
        print("ERREUR: La pizza existe deja")
    else:
        collection.append(pizza_utilisateur)


pizza = ["4 fromages", "vegetarienne", "hawai", "calzone"]
vide = ()
ajouter_pizza_utilisateur(pizza)
afficher(vide)

