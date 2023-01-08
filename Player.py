from time import sleep
from os import system
from random import randint
import platform
def clear():
    if platform.system()== "Windows":
        system('cls')
    else:
        system('clear')
from entite import Entite
from Classes_mechants.Geant import Geant

class Joueur(Entite):
    def __init__(self,nom,hp,force,defense,classe):
        super().__init__(nom,hp,force,defense,classe)
        self.inventaire=[]
        self.xp=0
        self.xp_requis=10
        self.executed = False

    def lvlup(self):
        self.xp+=randint(1,3)
        self.force+=randint(1,3)
        self.defense+=randint(1,3)
        self.xp=0
        self.xp_requis+=5


    def ajout_inv(self,item):
        self.inventaire.append(item)

    def use_item(self,item):
        pass



