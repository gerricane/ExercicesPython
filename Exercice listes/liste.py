personne = ["Mélanie", "Jean", "Martin", "Alice"]
nouvelle_personne = "David"

#print(personne)

personne.append(nouvelle_personne)
del personne[1]

#print(personne)

def afficher_personnes(c):
    for i in personne:
        print(i)

afficher_personnes(personne)

def modifier_valeur(a):
    a[0]= 10


test = [1,2,3,4]
modifier_valeur(test)
print(test)