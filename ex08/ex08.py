def afficher_pyramide(n):
    for i in range(1, n + 1):
        espaces = " " * (n - i)
        etoiles = "*" * (2 * i - 1)
        print(espaces + etoiles)

# Demander à l'utilisateur le nombre de lignes de la pyramide
while True:
    try:
        nombre_lignes = int(input("Entrez le nombre de lignes de la pyramide d'étoiles : "))
        if nombre_lignes <= 0:
            raise ValueError
        break
    except ValueError:
        print("Veuillez entrer un entier positif.")

# Afficher la pyramide d'étoiles
afficher_pyramide(nombre_lignes)
