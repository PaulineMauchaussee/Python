"""
    Ecrire un algo qui demande un nombre entier positif et qui nous retourne le carré de ce nombre
    Un carré est le résultat de la multiplication du nombre par lui même
    On peux pousser un peux et ajouter la vérification de la donnée avec une boucle "while"
"""


# saisir le nombre 

nombre = int(input("Ecrivez un nombre positif"))

nombre = nombre * nombre 
print(nombre)

nombre *=nombre
print(nombre)