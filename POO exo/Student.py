"""
Écrivez une classe appelée « Student » avec les membres suivant :
    •nom (de type String),
    •note1, note2 (de type int)
Le programme demande à l’utilisateur d’entrer le nom et les notes. calc_moy() calcule la note 
moyenne et show() affiche le nom et la note moyenne
"""

class Student():
    def __init__(self):
        nom, note1, note2 = self.entree()
        self.nom = nom
        self.note1 = note1
        self.note2 = note2

    

    #Ecriture des guetters nom et note1 et note2 (toujours mettre les getters avant les setters)
    
    @property
    def nom(self):
        return self.__nom
    
    @property
    def note1(self):
        return self.__note1
    
    @property
    def note2(self):
        return self.__note2
    
    #Ecriture des setters nom, note1 et note2 
    @note2.setter
    def note2(self, valeur):
        if type(valeur) == int or type(valeur) == float:                    # Gestion d'erreur, si la valeur est un int ou un float :
            self.__note2 = valeur                                            #Alors self.__longeur prend la valeur donné dans le paramètre valeur
        else:                                                               # Sinon (la valeur entrée n'est pas int ou float)
            raise TypeError("il faut un nombre") 


    @note1.setter
    def note1(self, valeur):
        if type(valeur) == int or type(valeur) == float:                    # Gestion d'erreur, si la valeur est un int ou un float :
            self.__note1 = valeur                                            #Alors self.__longeur prend la valeur donné dans le paramètre valeur
        else:                                                               # Sinon (la valeur entrée n'est pas int ou float)
            raise TypeError("il faut un nombre") 
        
    @nom.setter
    def nom(self,nom_personne):
        self.__nom = nom_personne


    #Ecrire une entrée pour que la personne puisse entrer son nom, note1 et note2 
    def entree(self):
        nom = input("Entrez votre nom : ")
        note1 = int(input("Entrez votre première note : "))
        note2 = int(input("Entrez votre seconde note : "))
        return nom,note1,note2


    #définir la moyenne de la personne avec ses notes 1 et 2 
    def moyenne(self):
        return(self.note1 + self.note2)/2
    
     
    
    #définir une chaine de caractère pour lorsque l'on print l'ojet on retrouve notre phrase
    def show(self) -> str:
        return "La moyenne de {0} a les notes suivantes {1}/20 et {2}/20. Sa moyenne est de {3}/20" .format(self.nom, self.note1, self.note2, int(self.moyenne()))
    



     
    





