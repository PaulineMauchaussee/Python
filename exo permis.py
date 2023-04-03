#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 21:07:49 2023

@author: pauline-mauchaussee
"""

"""
Permis :

Un permis de chasse à points possède au départ 
un capital de 100 points.

Si le chasseur tire sur (on sait pas si la cibl à survecue) :
    - une poule, il perd 1 point,
    - un chien, il perd 3 points,
    - une vache, il perd 5 points,
    - un autre chasseur, il perd 25.

Écrire un script qui  permet de calculer le nombre de point perdus.
sachant qu'un permis coute 200 euros,
calculer en fonction de son tableau de chasse,
le cout déboursé par ce chasseur.

"""

#Etape1 Ecrire une entrée pour chaque tire en fonction de la cible et du nombre de tire 
#Etape2 Ecrire un compteur qui démarre de 0
#Etape3 Ecrire les conditions en fonction des pertes de point (utiliser un dictionnaire)
#Etape4 Calculer la somme déboursée par le chasseur s'il perd son permis en fonction des points perdus 

capital_point=100
compteur=0
permis=200


def inputnombre(entrer):
    nombre=int(input(entrer))
    return nombre

def safari():
    poule = int(input("Ecrire le nombre de fois où vous avez tiré sur une poule: "))
    chien = int(input("Ecrire le nombre de fois où vous avez tiré sur une chien: "))
    vache = int(input("Ecrire le nombre de fois où vous avez tiré sur une vache: "))
    chasseur = int(input("Ecrire le nombre de fois où vous avez tiré sur une chasseur: "))

    return poule, chien, vache, chasseur 

def pertepoints(poule,chien,vache,chasseur):
    pointsperdus = poule + chasseur*3 +vache*5 + chasseur*25
    if pointsperdus > 0:
        print("Le chasseur a perdu" +str(pointsperdus)+"points")
    else:
        print("Le chasseur ,'a pas perddu de point")
    return pointsperdus

def permisperdu(nombre):
    nbpermis =0
    while nombre > 99 :
        nombre -=100
        nbpermis+=1
    if nombre <0:
        nombre = abs(nombre)
    else:
        nombre =100
        return (200*nbpermis), nombre

def main():
    poule, chien, vache, chasseur= safari()
    pointsperdus=pertepoints(poule, chien, vache, chasseur)
    payer, reste= permisperdu(pointsperdus)
    print("Le cout reviens a :")
    if payer==0:
        print("rien à payer")
    else:
        print(payer,"euros")
    print("il lui reste:" + str(reste)+ "points")
   


main()
