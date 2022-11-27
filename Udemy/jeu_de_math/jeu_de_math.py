import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION= 5


def poser_question() -> bool:
    a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    operators_str = ["+", "*"]
    chosen_operator = random.choice(operators_str)
    reponse_str = input(f"Calculez {a} {chosen_operator} {b} = ")
    reponse_int = int(reponse_str)
    if chosen_operator == "+":
        calcul = a + b
    else:
        calcul = a * b
    return reponse_int == calcul


nb_points = 0
for i in range(NB_QUESTION):
    print(f"Question n°{i+1} sur {NB_QUESTION}")
    if poser_question():
        print("Réponse correcte")
        nb_points += 1
    else:
        print("Réponse incorrecte")
    print()


print(f"Votre note: {nb_points} sur {NB_QUESTION}")
moyenne = NB_QUESTION // 2
if nb_points == NB_QUESTION:
    print("Excellent")
elif nb_points == 0:
    print("Révisez vos maths")
elif nb_points > moyenne:
    print("Pas mal")
else:
    print("Peut mieux faire")

