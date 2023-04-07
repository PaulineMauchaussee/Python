class Rectangle:
    def __init__(self, long, larg):
        self.largeur = larg
        self.longueur = long 


#Ecriture des guetters longueur et largeur (toujours mettre les getters avant les setters)
    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur 
    


#Ecriture des setters longueur et largeur 
    @longueur.setter
    def longueur(self, valeur):
        if type(valeur) == int or type(valeur) == float:                    # Gestion d'erreur, si la valeur est un int ou un float :
            self.__longueur = valeur                                            #Alors self.__longeur prend la valeur donné dans le paramètre valeur
        else:                                                               # Sinon (la valeur entrée n'est pas int ou float)
            raise TypeError("il faut un nombre") 


    @largeur.setter
    def largeur(self, valeur):
        if type(valeur) == int or type(valeur) == float:                    # Gestion d'erreur, si la valeur est un int ou un float :
            self.__largeur = valeur                                            #Alors self.__longeur prend la valeur donné dans le paramètre valeur
        else:                                                               # Sinon (la valeur entrée n'est pas int ou float)
            raise TypeError("il faut un nombre") 
    


    #définir la surface du rectangle en faisant longueur * largeur 
    def surface(self):
        return(self.__longueur * self.__largeur)
    

    #définir une chaine de caractère pour lorsque l'on print l'ojet on retrouve notre phrase
    def __str__(self) -> str:
        return "La surfuce du rectangle vaut : {}".format(self.surface())
        

    
