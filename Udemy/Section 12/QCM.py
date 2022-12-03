# Projet questionnaire
# Formation Python by Jonathan Roux.


def reponse_de_utilisateur():
    reponse_utilisateur = ""
    while reponse_utilisateur not in ['a', 'b', 'c', 'd']:
        reponse_utilisateur = input("Votre réponse: ")
        return reponse_utilisateur

def reponse(reponse: str, bonne_reponse: str):
    if reponse == bonne_reponse:
        print("Bonne réponse")
        print()
    else:
        print("Mauvaise réponse")
        print()

print("Quelle est la capitale de la france ?")
print("a) Marseille")
print("b) Nice")
print("c) Paris")
print("d) Nantes")

ma_reponse = reponse_de_utilisateur()
reponse(ma_reponse, "c")

print("Question 2: ")
print("Quelle est la capitale de l'Italie ?")
print("a) Turin")
print("b) Rome")
print("c) Naples")
print("d) Venise")

ma_reponse = reponse_de_utilisateur()
reponse(ma_reponse, "b")

print("Question 3: ")
print("Quelle est la capitale de la Belgique ?")
print("a) Bruxelles")
print("b) Charleroi")
print("c) Mons")
print("d) Bruges")

ma_reponse = reponse_de_utilisateur()
reponse(ma_reponse, "a")

print("Question 4: ")
print("Quelle est la capitale de l'Allemagne ?")
print("a) Hambourg")
print("b) Dresde")
print("c) Munich")
print("d) Berlin")

ma_reponse = reponse_de_utilisateur()
reponse(ma_reponse, "d")

print("Fin du questionnaire")