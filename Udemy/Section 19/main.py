def poser_question(question):
    choix = question[1]
    bonne_reponse = question[2]
    global score
    print("QUESTION")
    print("  " + question[0])
    # print("  ", choix[0])
    # print("  ", choix[1])
    # print("  ", choix[2])
    # print("  ", choix[3])
    for i in range(len(choix)):
        print("  ", choix[i])
    print()
    reponse = input("Votre réponse : ")
    if reponse.lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")

    print()


score = 0

'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
question3 = ("Quelle est la capitale de la la Belgique ?", ("Charleroi", "Bruxelles", "Gand", "Mons", "Liege"), "Bruxelles")

poser_question(question1)
poser_question(question2)
poser_question(question3)


print("Score final :", score)
