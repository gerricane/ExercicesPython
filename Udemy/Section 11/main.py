def afficher_table_multiplication(n_table, min=1, max=10):
    if min < max :
        print("Le min est superieur au max")
        return

    print(f"Table de {n_table}")
    for i in range(min,max+1):
        resultat = i * n_table
        print(f"{i} x {n_table} = {resultat}")


afficher_table_multiplication(9)