class Voiture :
    def __init__(self, matricule,marque,coul):
        self.matricule = matricule
        self.marque = marque
        self.couleur = coul
        self.etat = False
    def afficher_infos(self):
        print(f"la voiture : {self.matricule} , de marque : {self.marque} , de couleur : {self.couleur}")

    def voiture_stocke(self):
        self.etat = True
        print(f"la voiture : {self.matricule} est stocke")
    def voiture_sortie(self):
        self.etat = False
        print(f"la voiture : {self.matricule} est sortie")

