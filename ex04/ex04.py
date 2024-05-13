def tri_croissant(tableau):
    for i in range(1, len(tableau)):
        valeur_actuelle = tableau[i]
        position = i

        while position > 0 and tableau[position - 1] > valeur_actuelle:
            tableau[position] = tableau[position - 1]
            position -= 1

        tableau[position] = valeur_actuelle

    return tableau

# Générer un tableau d'entiers aléatoires avec plus de 15 éléments
import random
taille = 20
tableau_aléatoire = [random.randint(1, 100) for _ in range(taille)]

# Afficher le tableau avant le tri
print("Tableau avant le tri :", tableau_aléatoire)

# Trier le tableau par ordre croissant
tableau_trié = tri_croissant(tableau_aléatoire)

# Afficher le tableau après le tri
print("Tableau après le tri :", tableau_trié)
