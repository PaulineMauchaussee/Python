liste= [8, 5, 1, 7, 6, 4]

print("voici la liste avant le tri ")
print(liste)

for i in range(len(liste)):
    min_index = i
    for j in range (i+1, len (liste)):
        if liste [j] < liste[min_index]:
            min_index =j
    liste[i], liste[min_index] = liste[min_index] ,  liste[i]

    
