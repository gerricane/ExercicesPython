def recuper_et_afficher_infos_personne(numero_personne):
    nom = input(f"Nom de la personne {numero_personne}: ")
    age = input(f"Age de la personne {numero_personne}: ")
    print(f"La personne {numero_personne} est {nom}, son age est {age} ans")
    print(f"Le nom comporte {len(nom)} lettres")


#recuper_et_afficher_infos_personne(1)

# nb_personne = input("Combien de personne seront presente ? ")
# nb_personne_int = int(nb_personne)
# for i in range (1,nb_personne_int+1):
#     recuper_et_afficher_infos_personne(i)

nb_personnes = 3
for i in range(nb_personnes):
    recuper_et_afficher_infos_personne(i+1)