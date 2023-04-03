"""
    Ecrire un algo qui demander 3 variable de type String qui sont des noms et qui va vérifier si il sont entrée dans l'ordre alphabétique
    On pourrait pousser l'exercice plus loin en triant les nom si il ne le sont pas de base 
"""

# ecrire trois variables de type string 

nom1= input("Entrez le nom 1")
nom2= input("Entrez le nom 2")
nom3= input("Entrez le nom 3")

print(nom1, nom2, nom3)

#vérifier s'ils sont dans l'ordre alpahbétique # 1 2 3
var=[nom1,nom2,nom3]
var2= var.copy()
var.sort()
var==var2
if var==var2:
    print("C'est trié")
else:
    print("C'est pas trié")

print(var)

