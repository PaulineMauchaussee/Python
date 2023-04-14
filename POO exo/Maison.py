"""
- Créez une classe « Maison », avec un attribut « surface », 
- un constructeur qui définit sa valeur 
- une méthode « Display » pour afficher « Je suis une maison, ma surface est de XXX m2 » (XXX: la valeur de 
surface).
- Incluez aussi des getters et des setters pour la surface.
La classe « Maison » contiendra une porte (Porte). 
Chaque porte aura un attribut « couleur » (de type 
String), et une méthode « Display » qui affichera « Je suis une porte, ma couleur est bleue » (ou quelle 
que soit la couleur). Inclure un getter et un setter. Créez également la méthode « GetPorte » dans la 
classe « Maison ».
La classe « Apartment » est une sous-classe de la classe « Maison », avec une surface prédéfinie de 
50m2.
Créez également une classe Person, avec un nom (de type String). Chaque personne aura une maison. 
La méthode « Display » pour une personne affichera son nom, les données de sa maison et les 
données de la porte de cette maison.
Écrivez un Main pour créer un Apartment, une personne pour y vivre et pour afficher les données de 
la personne
"""

class Porte:
    def __init__(self, couleur: str) -> None:
        self.__couleur = couleur
    def get_couleur(self):
        return self.__couleur
    def set_couleur(self, couleur):
        couleurs_auth = ["rouge", "bleue", "jaune"]
        if couleur in couleurs_auth:
            self.__couleur = couleur
        else:
            raise (
                f"Vous devez choisir une couleur dans la liste : {couleurs_auth}")
    def display(self):
        """_summary_
        """
        print(f"Je suis une porte, ma couleur est {self.__couleur}")

class Maison:
    def __init__(self, surface, porte: Porte = None):
        self.set_surface(surface)
        self.porte = porte
    def get_surface(self):
        return self.__surface
    def set_surface(self, surface):
        self.__surface = surface
    def get_porte(self):
        return self.porte
    def set_porte(self, porte):
        self.porte = porte
    def display(self):
        print(f"Je suis une maison, ma surface est de {self.get_surface()} m2")

class Apartment(Maison):
    def __init__(self, surface=50, porte: Porte = None):
        super().__init__(surface, porte)

class Person():
    def __init__(self, nom: str, maison: Maison):
        super().__init__()
        self.nom = nom
        self.maison = maison
    def display(self):
        """_summary_ : affiche le nom, la maison et la couleur de la porte
        """
        print(f"mon nom est {self.nom}")
        self.maison.display()
        porte = self.maison.get_porte()
        if (porte is None):
            print("pas de porte")
        else:
            porte.display()

if __name__ == "__main__":
    p1 = Porte("bleue")
    p1.display()
    m1 = Maison(100, p1)
    proprietaire1 = Person("Said", m1)
    proprietaire1.display()
    print("--------------------------")
    p2 = Porte("verte")
    a2 = Apartment(500, p2)
    proprietaire2 = Person("Truc", a2)
    proprietaire2.display()