"""

Calcul d'un prix TTC.

Creer un script qui demande le prix hors taxe
d'un article.
Pus qui demande si l'article est de la nourriture
ou non.
Le script doit calculer le prix ttc selon si
c'est de la nourriture ou non.

rappel, pour les biens communs la TVA c'est 20.0%
sinon c'est 5.5% pour la nourriture

"""
# saisie de deux valeurs : prix et article 
prix= float(input("Quel est le prix hors taxe ? "))
condition = input("Est-ce de la nourriture ?")

# créer une boucle pour savoir si l'article est de l'alimentaire ou non 
while condition not in ["oui", "non"]:
    condition= input("Est-ce de la nourriture ? (oui/non)")

# Si la condition "oui" est respectée on affiche 
if condition == "oui":
    print(f"le prix ttc ests de {prix*1.055} euros")
else:
    print(f"lee prix ttc est de {prix*1.20} euros")





