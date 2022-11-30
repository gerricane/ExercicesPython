import time


def cuisson (d_coque):
    while not d_coque == 0:
        min = d_coque // 60
        sec = d_coque - min * 60
        print(f"Temps restant: {min:02d}:{sec:02d} minutes", end="")
        for i in range(10):
            time.sleep(1)
            print(".", end="", flush=True)
            d_coque -= 1
            min = d_coque // 60
            sec = d_coque - min * 60
        print()
    print("Cuisson terminée")

    
choix_str = ""
print("a) Oeuf a la coque: 3 min")
print("b) Oeuf mollets: 6 min")
print("c) Oeuf dur: 9 min")
print("0 pour sortir")
while choix_str not in ["a","b", "c", "d", "0"]:
    choix_str = input("Quelle cuissson les oeufs ? ")
if choix_str == "a":
    cuisson(180)
elif choix_str == "b":
    cuisson(360)
elif choix_str == "c":
    cuisson(540)
