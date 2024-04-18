# -*- coding: utf-8 -*-

#%% Classe Voiture 'Sortie usine'
class Voiture_avec_init:
    def __init__(self):
        self.nom='Peugeot'
        self.km=0
# Création d'une instance de la classe "Voiture_avec_init"         
voit1=Voiture_avec_init()
print(voit1.km,voit1.nom)



#%% Classe Voiture 'Vendeur véhicule occasion'
class Voiture:
    def __init__(self,val_nom,val_km):
        self.nom=val_nom
        self.km=float(val_km)
    def ajoute_km_trajet(self,trajet):
        self.km=self.km+float(trajet)

# Création d'une instance de la classe "Voiture"         
voit2=Voiture('Renault','2000')
print(voit2.km,voit2.nom)
# Utilisation de la fonction ajoute_km_trajet
voit2.ajoute_km_trajet('220')
print(voit2.km)
voit2.km='3000'


#%%
class Voiture:
    def __init__(self,val_nom,val_km):
        self.nom=val_nom
        self.km=float(val_km)
    def ajoute_km_trajet(self,trajet):
        self._km=self._km+float(trajet)
    def _get_km(self):
        print('Kilométrage en cours')
        self._km
        return self._km
    def _set_km(self,v):
        print('Kilométrage MAJ')
        self._km=v
        return self._km
    km=property(_get_km,_set_km)    
        
voit2=Voiture('Renault','2000')
print(voit2.km,voit2.nom)
voit2.ajoute_km_trajet('220')
print(voit2.km)
voit2.km='3000'
#%%
class Voiture:
    def __init__(self,val_nom,val_km):
        self.nom=val_nom
        self.km=float(val_km)
    def _get_km(self):
        print('Kilométrage en cours')
        self._km
        return self._km
    def _set_km(self,v):
        print('Kilométrage MAJ')
        self._km=v
        return self._km
    km=property(_get_km,_set_km)    
        
voit2=Voiture('Renault','2000')
print(voit2.km,voit2.nom)
voit2.ajoute_km_trajet('220')
print(voit2.km)
voit2.km='3000'

