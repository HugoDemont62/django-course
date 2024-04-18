class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def aire(self):
        return self.x*self.y
class Carre(Rectangle):
    def __init__(self,x):
        self.x=self.y=x

# # Création d'une instance rectangle
# Rec1=Rectangle(2,3)
# print(Rec1.aire(), 'm²')
# # Création d'une instance carré
# Car1=Carre(10)
# # Carre hérite de la fonction aire appartenant à la classe rectangle
# print(Car1.aire(), 'm²')

# print(Carre(5).aire())
