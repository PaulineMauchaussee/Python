from math import sqrt

"""
Créez une classe appelée « Point ». Cette classe doit avoir 2 entiers (x, y) en tant que membres privés. 
Le constructeur doit définir les valeurs de x et y via des paramètres. La classe doit avoir une méthode 
publique appelée « distance ». Cela prend un seul paramètre(Point) et renvoie la distance entre les 2 
points
"""

class Point():
    def __init__(self,x,y):
        self.__x =x
        self.__y = y



#Ecriture des getters x et Y (récupérer les données)
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
#Ecriture des setters x et y 

    @x.setter
    def x(self,valeur):
        if valeur == int or valeur == float:
            self.__x=valeur
        else:
            raise TypeError("Il faut un nombre")
    
    

    @y.setter
    def y(self,valeur):
        if valeur == int or valeur == float:
            self.__y=valeur
        else:
            raise TypeError("Il faut un nombre")

# définir la distance entre x et y 
    def distance(self, point):
        # c'est le premier point
        x1 = self.x
        y1 = self.y

        # c'est le deuxième point
        x2 = point.x
        y2 = point.y

        # calcul de la distance 
        distance = sqrt((x1-x2)**2 + (y1-y2)**2)
        
        return distance
    

    

    
    
        
    

    
   

