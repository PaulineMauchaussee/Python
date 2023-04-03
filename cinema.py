# Saisir les valeurs prix et age 
prix = {"mineur":5 , "majeur":10}
age = input ("Saisir  mineur ou majeur ")

# vérifier la  saisie de l'utilisateur  
if age == "mineur":
    prix_entree =prix ["mineur"]
else:
    prix_entree = prix["majeur"]

# imprimer le prix d'entrée 
print("le prix d'entrée est de" , prix_entree)

