nombre = int(input("Entrez un nombre"))
while nombre <=1 :
    nombre = int(input("jai dit un nombre entier posifif"))

diviseur=2
compteur=0
moitier=nombre/2

while diviseur <=moitier:
    if nombre % diviseur == 0:
        compteur += 1
        print(diviseur)
    diviseur += 1 
if not compteur:
    print("il est premier")
else:
    print(compteur,diviseur)
