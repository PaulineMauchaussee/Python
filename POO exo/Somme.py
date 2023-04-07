"""
Écrivez une classe « Somme » ayant deux variables « n1 » et « n2 » et une fonction membre « sum() » 
qui calcule la somme. Dans la méthode principale main demandez à l’utilisateur d’entrez deux entiers 
et passez-les au constructeur par défaut de la classe « Somme » et afficher le résultat de l’addition des 
deux nombres
"""

class Somme():
    def __init__(self,n1,n2):
        self.numero1 = n1
        self.numero2 = n2


#Ecriture des guetters numero1 et numéro2 (toujours mettre les getters avant les setters)
    @property
    def numero1(self):
        return self.__numero1
    
    @property
    def numero2(self):
        return self.__numero2
    

#Ecriture des setters numero1 et numero2
    @numero1.setter
    def numero1(self, valeur):
        if type(valeur) == int or type(valeur) == float:                    # Gestion d'erreur, si la valeur est un int ou un float :
            self.__numero1 = valeur                                            #Alors self.__longeur prend la valeur donné dans le paramètre valeur
        else:                                                               # Sinon (la valeur entrée n'est pas int ou float)
            raise TypeError("il faut un nombre") 


    @numero2.setter
    def numero2(self, valeur):
        if type(valeur) == int or type(valeur) == float:                    # Gestion d'erreur, si la valeur est un int ou un float :
            self.__numero2 = valeur                                            #Alors self.__longeur prend la valeur donné dans le paramètre valeur
        else:                                                               # Sinon (la valeur entrée n'est pas int ou float)
            raise TypeError("il faut un nombre") 
    

    #définir la somme du numero 1 et du numéro 2
    def somme(self):
        return( self.numero1 + self.numero2)
    
    #définir une chaine de caractère pour lorsque l'on print l'ojet on retrouve notre phrase
    def __str__(self) -> str:
        return "La somme du numero1 et du numero2 : {}".format(self.somme())
    