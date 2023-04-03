"""
Train :

Un train est parti de la gare du Nord à 9 h
(il y a 170 km entre la gare du Nord et Arras).

Écrire un script qui affiche un tableau me permettant de connaître
l'heure à laquelle le train passe à Arras.

Le tableau prédira les différentes heures possibles:
pour toutes les vitesses de 100 km/h à 300 km/h, par pas de 10 km/h,
les résultats étant arrondis à la minute inférieure.

Écrire une fonction tchoutchou qui reçoit la vitesse du train et
qui affiche l'heure du passage;

Écrire le programme principal qui affiche le tableau demandé.

"""



#Ecrire une fonction avec les vitesses de 100 à 300 avec un pas de 10
def train():
    for i in range(100,310,10):
        tchoutchou(i)


def tchoutchou(a):
    temps= 170/a
    heure_arrivee =9+temps
    # convertir pour extraire les heures et les minutes 
    heures = int(heure_arrivee)
    minutes= int((heure_arrivee-heures)*60)
    #afficher le tableau avec les heures 
    print(f"{heures} : {minutes}")




train()