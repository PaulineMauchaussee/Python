#exo1
prenom = "Pauline"
print(f"Bonjour,{prenom}")

#exo2
prenom = input("quel est votre prénom?")
print(f"Bonjour,{prenom}")


#exo paire impaire

"""
Paire ou impaire

Creer un script qui demande un nombre.

le script doit afficher si le nombre est paire ou impaire

"""

entrer = int(input("entrez un nombre : "))


while entrer < 1:
    entrer = int(input("entrer un nombre supérieur à 1 svp"))

if entrer % 2 == 0:
    print(entrer, "est pair")
else:
    print(entrer, "est impair")

#EXOpuissance2

"""
Puissance 2 

Ecrire un script qui determine le nombre de fois qu'un nombre est divisible par 2
"""


nombre = int(input("Entrez un nombre"))
compteur = 0

while nombre%2 == 0:
    nombre = nombre/2
    compteur = compteur + 1

print(compteur)

if nombre!=1:
    print("il reste :",nombre , "qui n'est pas 2")
else:
    print("c'est une puissance de 2 :2^", compteur)
  







