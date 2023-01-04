
class Entite:
    def __init__(self,nom,hp,force,defense,classe):
        self.nom=nom
        self.hp=hp
        self.force=force
        self.defense=defense
        self.classe=classe
        self.poisoned = False
        self.poison_dura = 0


    def recevoir_degat(self,dmg):
        self.hp -= dmg
        if self.hp<0:
            self.hp=0

    def infliger_degat(self,cible):
            dmg=self.force-cible.defense
            cible.recevoir_degat(dmg)

    def update_poison_status(self):
        if self.poisoned:
            poison_dmg = 5
            self.hp -= poison_dmg
            self.poison_dura -= 1
            if self.poison_dura == 0:
                self.poisoned = False

    def update_execute_status(self, player,ennemi):
            if self.classe=="Geant":
                execute_seuil = self.hp * 0.15
                if self.hp <= execute_seuil:
                    self.executed = True
                    self.hp = 0
                    print(f"{player.nom} a été exécuté par {self.nom}!")
            else:
                return None

