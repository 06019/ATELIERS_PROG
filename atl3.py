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

class Parc :
    def __init__(self,id,adr,cap):
        self.identifiant = id
        self.adresse= adr
        self.capacite = cap
        self.liste_voitures = []
    def entrer_voiture(self,voiture):
        for v in self.liste_voitures:
            if v.matricule == voiture.matricule:
                print ("votre voiture existe deja ")
                return
        if len(self.liste_voitures)>= self.capacite:
            print ("desole le parc est plien y a plus d'espace")
            return
        self.liste_voitures.append(voiture)
        voiture.voiture_stocke()
        print ("votre voiture stocke")



