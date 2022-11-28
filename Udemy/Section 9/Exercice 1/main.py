# Exercice 1 de la section 9: Epreuve de code
#Par Sebastien


NB_POUCES = 2.54
nb_a_convertir_str = input("Nombre a convetir en pouces: ")
nb_a_convertir_flo = float(nb_a_convertir_str)
resultat = nb_a_convertir_flo / NB_POUCES

print(f"{nb_a_convertir_flo} cm donne {resultat}")