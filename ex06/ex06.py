def longueur_chaine(chaine):
    count = 0
    for caractere in chaine:
        count += 1
    return count


chaine = "Bonjour, monde!"
longueur = longueur_chaine(chaine)
print("La longueur de la chaîne est :", longueur)
