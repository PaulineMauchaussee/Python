"""
    Ecrire un programme de tri a bulle:

    Le principe du tri a bulle est de comparer un element d'un tableau 
    avec son voisin suivant,
    si l'element est plus grand que son voisin, on inverse les positions
    sinon passe à l'élément suivant
    Astuce :
        Au lieu de passer par une variable temporaire
        python permet de swap:
            liste[i], liste[i+1] = liste[i+1], liste[i]

"""

# ETAPE1créer une fonction pour créer une liste 
# Etape2

def triebulle():
    liste= [1,4,5,2,1,4,5,2,1,4,5,2,1,4,5,2]
    taille=len(liste)
    compteur=1

    print(liste)
   
    while compteur >0:
    # on va répéter plusieurs les permutations jusqu'à ce que tout soit trié (il n'y a plus de permutation à faire) 
        compteur=0
        # boucle pour permuter les éléments de toute la liste 
        for i in range(taille-1):
            # print(i, "la valeur i")
            if liste[i] > liste[i+1]:
                compteur+=1
                liste[i], liste[i+1] = liste[i+1], liste[i]

    print(liste)





triebulle()