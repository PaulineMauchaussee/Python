

"""
    Ecrire un algo qui demande deux nombre a l'utilisateur et qui va vérifier si le produit des deux nombre est positif ou négatif ou nul
    Mais on ne réalise pas le calcul
"""

# Faire Saisir deux nombres à l'utilisateur 
from operator import xor


nombre1 = int(input("Ecrivez premier nombre :  "))
nombre2 = int(input("Ecrivez deuxième nombre :  "))


if nombre1 == 0 or nombre2 == 0:
    print("leur produit est nul")
elif (nombre1>1 and nombre2>0) or(nombre1<0 and nombre2<0):
        print("leur produit est positif")
else:
      print("leur produit est négatif)")







