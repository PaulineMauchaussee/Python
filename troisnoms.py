"""
    Ecrire un algo qui demander 3 variable de type String qui sont des noms et qui va vérifier si il sont entrée dans l'ordre alphabétique
    On pourrait pousser l'exercice plus loin en triant les nom si il ne le sont pas de base 
"""

# ecrire trois variables de type string 

nom1= input("Entrez le nom 1")
nom2= input("Entrez le nom 2")
nom3= input("Entrez le nom 3")

print(nom1, nom2, nom3)

#vérifier s'ils sont dans l'ordre alpahbétique # 1 2 3

if nom1<=nom2 <=nom3:
    print("Les noms sont rangés dans l'ordre alphabiétique")
else:
    print("Les noms ne sont pas rangés dans l'ordre alphabiétique")


def trie():
    trie= []
    trie.append(nom1)
    trie.append(nom2)
    trie.append(nom3)
    trie.sort()
    trie = ", ".join(trie)
    print ("une fois trié cela donnerai :", trie)
    
trie()




