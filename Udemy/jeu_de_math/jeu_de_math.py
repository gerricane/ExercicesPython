import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION= 5


def poser_question():
    a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o =random.randint(0,1)
    operateur_str = "+"
    if o == 1:
        operateur_str= "*"
    reponse_str = input(f"Calculez {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a+b
    if o == 1:
        calcul = a*b
    if reponse_int == calcul:
        return True

    return False



#poser_question()

nb_points = 0
for i in range(0,NB_QUESTION):
    print(f"Question n°{i+1} sur {NB_QUESTION}")
    pts=poser_question()
    if pts == True:
        print("Réponse correcte")
        nb_points += 1
    else:
        print("Réponse incorrect")
    print()

print(f"Votre note: {nb_points} sur {NB_QUESTION}")
moyenne = int(NB_QUESTION/2)
if nb_points == NB_QUESTION:
    print("Excellent")
elif nb_points == 0:
    print("Revisez vos maths")
elif nb_points > moyenne:
    print("pas mal")
else:
    print("peut mieux faire")

