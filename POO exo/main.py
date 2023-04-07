from Mesmodules import Rectangle
from Somme import Somme
from Student import Student
from Point import Point 

def fonction_rectangle():
    rectangle = Rectangle(10, 5)

    print(rectangle)




def fonction_somme():
    somme = Somme(10,5)

    print(somme)





def fonction_etudiant():
    moyenne = Student()

    print(moyenne.show())


def fonction_point():
    point1 = Point(3, 5)
    point2 = Point(5, 6)

    print(point1.distance(point2))

fonction_point()
