class Sorcier:
    def __init__(self,nom,hp,force,defense,nbr_potions):
        super().__init__(nom,hp,force,defense)
        self.nbr_potions=nbr_potions

    def soin(self):
        if self.nbr_potions>0:
            self.hp+=10
            self.nbr_potions-=1