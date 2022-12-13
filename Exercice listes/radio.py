radio = ["Skyrock","France Bleu", "Chante France", "RFM"]
choix_int = 0

def choix_radio(choix_utilisateur, radio):
    print(f"Lecture de la radio {radio[choix_utilisateur-1]}")


for i in range (len(radio)):
    print(i+1,"-", radio[i])

while True:
    choix_str = input(f"Faites un choix entre 1 et {len(radio)}: ")
    if choix_str == "":
        break
    choix_int = int(choix_str)
    if choix_int <= (len(radio)):
        choix_radio(choix_int, radio)
    else:
        print("Erreur")

