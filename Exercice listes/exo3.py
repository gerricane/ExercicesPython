def afficher_pizza(collection):
    nb_pizza = len(collection)
    if nb_pizza == 0:
        print("Aucune pizza")
        return
    else:
        print(f"---- Liste des pizza ({len(collection)}) ----")
        for i in collection:
            print(i)
        print()
        print("Premiere pizza: ", collection[0])
        print("Derniere pizza: ", collection[-1])

pizza = ["4 fromages", "vegetarienne", "hawai", "calzone"]

vide = ()

afficher_pizza(pizza)
