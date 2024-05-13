import random

def tri_décroissant(tableau):
    for i in range(len(tableau)):
        for j in range(i+1, len(tableau)):
            if tableau[i] < tableau[j]:
                tableau[i], tableau[j] = tableau[j], tableau[i]
    return tableau


taille = 20
tableau_aléatoire = [random.randint(1, 100) for _ in range(taille)]


print("Tableau avant le tri :", tableau_aléatoire)


tableau_trié = tri_décroissant(tableau_aléatoire)


print("Tableau après le tri décroissant :", tableau_trié)
