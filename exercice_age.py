age = int(input("Entrez l'âge de l'enfant"))

if age >= 12:
    print("cadet")
elif age >= 10:
    print("Minime")
elif age >= 8:
    print("Pupille")
else:
    print("poussin")