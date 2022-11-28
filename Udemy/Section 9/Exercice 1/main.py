# Exercice 1 de la section 9: Epreuve de code
#Par Sebastien

# Variable

def conv_en_cm(nb_pouces):
    print(nb_pouces)
    return 0

def conv_en_pouces(nb_cm):
    print(nb_pouces)
    return 0


menu_int = 0
nb_en_pouces_floa = 0

print("1: Conversion pouces vers cm")
print("2: Conversion cm vers pouces")
while menu_int == 0:
    menu_str = input("Votre choix ? ")
    try:
        menu_int = int(menu_str)
    except:
        print("Il me faut un numero")

if menu_int == 1:
    while nb_en_pouces_floa == 0:
        nb_en_pouce_str = input("Combien de pouces ? ")
        try:
            nb_en_pouces_floa = float(nb_en_pouce_str)
        except:
            print("J'attend un nombre")
conv_en_cm(nb_en_pouces_floa)
