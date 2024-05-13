def est_nombre_armstrong(num):
    # Convertir le nombre en chaîne de caractères pour accéder à chaque chiffre
    chiffres = str(num)
    longueur = len(chiffres)
    somme = 0
    
    # Calculer la somme des cubes de chaque chiffre
    for chiffre in chiffres:
        somme += int(chiffre) ** longueur
    
    # Vérifier si la somme est égale au nombre lui-même
    if somme == num:
        return True
    else:
        return False

# Demander à l'utilisateur d'entrer un numéro
numero = int(input("Entrez un numéro : "))

# Vérifier si le numéro est un nombre Armstrong
if est_nombre_armstrong(numero) and len(str(numero)) == 3:
    print(numero, "est un nombre Armstrong")
else:
    print(numero, "n'est pas un nombre Armstrong")
