"""

Suite100

Creer un script qui demande une suite
de nombres positifs ou nuls.

calculez la somme de cette suite
à chaque nombre ajouté.
Comptez combien il y avait de données et
combien étaient supérieures à 100.

afficher le resultat et continer.

Entrer un nombre inférieur à 0 indique la fin de la suite.
"""

 # définir une fonction 

# def suite100():
#         #créer ma liste 


ma_liste = []

while True: 
    nombre= (int(input("Entrez un nombre positif ou nul")))
    if nombre <=0:
        break
    ma_liste.append(nombre)

print(ma_liste)

### conversion
variable = [int(index) for index in ma_liste]


compteur=0
#compte le nombre qui est supérieur à 100

for index in variable :
    if index>100:
        compteur+=1

print(compteur)
 








