#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ecrire l'algorithme de la suite de fibonacci:

C'est une suite définie par Un = Un-1 + Un-2

Si vous trouvez ça trop facile, passez par une fonction récursive
( c'est à dire fonction qui s'appelle elle meme)

ex: 
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610
"""




#déclarer une fonction fibonacci

def fibonacci():
    nombre= int(input("Entrez un nombre: "))
    fibonacci = [0]*( nombre) 
    #initialiser la liste 
    fibonacci[0] = 0 
    fibonacci[1]= 1

    for i in range (2,nombre):
        fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]
    print(fibonacci)



fibonacci() 