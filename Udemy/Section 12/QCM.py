# Projet questionnaire
# Formation Python by Jonathan Roux.


def reponse_de_utilisateur():
    reponse_utilisateur = ""
    while reponse_utilisateur not in ['a', 'b', 'c', 'd']:
        reponse_utilisateur = input("Votre réponse: ")
        return reponse_utilisateur

def poser_question(question, r1, r2, r3, r4):
    print(question)
    print(f"a) {r1}")
    print(f"b) {r2}")
    print(f"c) {r3}")
    print(f"d) {r4}")

def reponse(reponse: str, bonne_reponse: str):
    if reponse == bonne_reponse:
        print("Bonne réponse")
        print()
    else:
        print("Mauvaise réponse")
        print()


poser_question("Quelle est la capitale de la france ?","Marseille", "Nice", "Paris", "Nantes")
ma_reponse = reponse_de_utilisateur()
reponse(ma_reponse, "c")

poser_question("Quelle est la capitale de l'Italie ?","Turin", "Rome", "Naples", "Venise")
ma_reponse = reponse_de_utilisateur()
reponse(ma_reponse, "b")

poser_question("Quelle est la capitale de la Belgique ?","Bruxelles", "Charleroi", "Mons", "Bruges")
ma_reponse = reponse_de_utilisateur()
reponse(ma_reponse, "a")

poser_question("Quelle est la capitale de l'Allemagne ?","Hambourg", "Dresde", "Munich", "Berlin")
ma_reponse = reponse_de_utilisateur()
reponse(ma_reponse, "d")

print("Fin du questionnaire")