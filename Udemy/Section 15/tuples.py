# Collections : Tableaux, listes, tuples
# Plusieurs éléments
# Tuples() = immutable -> non modifiable
# Liste [] = mutable -> modifiable
# -1 pour le dernier éléments


#personnes = ("Mélanie", "Jean", "Martin", "Alice")
# print(personnes[2])
#
# for i in range(0, len(personnes)):
#     print(personnes[i])
#
#
# for i in personnes:
#     print(i)


# ------------ Liste -------------------------
personnes = ["Mélanie", "Jean", "Martin", "Alice"]
nouvelle_personne = "David"

personnes.append(nouvelle_personne)

print(personnes)

for i in personnes:
    print(i)
    print(personnes.index(i))