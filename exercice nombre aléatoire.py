# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 19:27:18 2023

@author: pasca
"""

"""

But de l'exercice :
    
Votre programme génère un nombre aléatoire entre 1 et 1 000.

Il demande ensuite à l'utilisateur de proposer un nombre.

L'utilisateur entre un nombre dans la console :
    - Si celui-ci est plus petit que le nombre généré, le programme affiche :
    "C'est PLUS !" et demande un nouveau nombre.
    - Si celui-ci est plus grand que le nombre généré, le programme affiche :
    "C'est MOINS !" et demande un nouveau nombre.
    - Si celui-ci est le nombre généré aléatoirement, le programme affiche :
    "C'est GAGNÉ !" puis l'exécution du programme se termine.

Le nombre d'essaie de l'utilisateur est limité à 10 :
    - Chaque tour, le programme affiche le nombre de tours restants à
    l'utilisateur
    - Si au bout de 10 essais l'utilisateur n'a pas trouvé le nombre,
    le programme affiche : "C'est PERDU ! Le nombre était : nombreAleatoire"
    puis l'exécution du programme se termine.

"""

#Etape1 Créer une variable pour générer un nombre aléatoire entre 1 et 1000 avec randint
import random 
nombre_aleatoire = random.randint(1,1001)
print(nombre_aleatoire)
#Etape2 Créer une entrée pour l'utilisateur pour un nombre 
nombre= int(input("Entrez votre nombre"))


#Etape4 Mettre en place un compteur pour afficher le nombre de tour restant 
compteur=0
#Etape3 créer une boucle tant que le nombre est différents du nombre aléatoire tu rejoues, en metteant en place les conditions
while nombre!=nombre_aleatoire:  
    
    if compteur !=10: #Etape 5 mettre une condition si le compteur ddifférent de 10 alors le jeu break 
            compteur+=1
            if nombre<nombre_aleatoire:
     
                print("C'est plus")
                print("Il vous reste",10-compteur, "chances")
                nombre= int(input("Entrez à nouveau votre nombre"))
    
            elif nombre>nombre_aleatoire:
                print("C'est moins")
                print("Il vous reste",10-compteur, "chances")
                nombre= int(input("Entrez à nouveau votre nombre"))
            
    else:   
        print("C'est perdu")
        break
      
    
else:
    print("C'est gagné")


  




#Etape4 Limiter l'utilisateur à 10 chances en mettant un compteur 





        




        
