def afficher(collection):
    nb_pizzas = len(collection)
    if nb_pizzas == 0:
        print("---- Aucune Pizza ---")
    else:
        print(f" ---- LISTE DES PIZZAS ({nb_pizzas}) ----")
        for i in collection:
            print(i)
        print()
        print(f"Premiere pizza: {collection[0]}")
        print(f"Derniere pizza: {collection[-1]}")
# premiere pizza
# derniere pizza

pizza = ["4 fromages", "vegetarienne", "hawai", "calzone"]
#vide = ()
# ajouter_pizza_utilisateur(pizza)
afficher(pizza)

