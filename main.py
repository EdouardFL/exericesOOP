import random
import math

# Exercice 1:
class StringFoo:

    def __init__(self):
        self.string = None

    def set_string(self, parametre):
        self.string = parametre

    def print_string(self):
        print(str.upper(self.string))


newstring = StringFoo()
newstring.set_string("gkrkh")
newstring.print_string()

# -------------------------------------------------------------------
# Exercice 2:
# -------------------------------------------------------------------

class Rectangle:

    def __init__(self, largeur, longeur):
        self.largeur = largeur
        self.longeur = longeur
        self.air = None

    def calcute_aire(self):
        self.air = self.longeur * self.largeur

    def afficher_info(self):
        print("Largeur:", self.largeur, "\nLongeur:", self.longeur, "\nAir:", self.air)


Rect1 = Rectangle(5, 6)
Rect1.calcute_aire()
Rect1.afficher_info()

# -------------------------------------------------------------------
# Exercice 3:
# -------------------------------------------------------------------

class Cercle:

    def __init__(self, rayon):
        self.rayon = rayon

    def calcule_air(self):
        return math.pi * self.rayon * self.rayon

    def calcure_cir(self):
        return 2 * math.pi * self.rayon


Cercle1 = Cercle(6)
print(Cercle1.calcure_cir())
print(Cercle1.calcule_air())

# -------------------------------------------------------------------
# Exercice 4:
# -------------------------------------------------------------------

class Hero:

    def __init__(self, nom):
        self.pv = random.randint(1, 10) + random.randint(1, 10)
        self.force = random.randint(1, 6)
        self.defence = random.randint(1, 6)
        self.nom = nom

    def attaque(self):
        return self.force + random.randint(1, 6)

    def dommage(self, dmg):
        self.pv -= dmg - self.defence

    def est_vivant(self):
        if self.pv <= 0:
            return False
        else:
            return True


hero1 = Hero("Joe")
print(hero1.attaque())
hero1.dommage(5)
print(hero1.est_vivant())
