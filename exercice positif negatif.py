"""
    Ecrire un algo qui demande un nombre a l'utilisateur et qui va vérifier si ce nombre est positif ou négatif ou nul
    
"""
# Saisir un nombre à l'utilisateur 
nombre = int(input("Ecrivez un nombre positif"))

# vérifier que le nombre saisi est positif/négatif ou nul
if nombre > 0:
    print("le nombre est positif")
elif nombre == 0:
    print("le nombre est nul")
else:
    print("le nombre est négatif")
    


