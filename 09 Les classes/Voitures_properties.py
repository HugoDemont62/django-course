# -*- coding: utf-8 -*-

#%%
# coding: utf-8
class Voiture:
    def __init__(self,_km):  # _ est indispensable
        self.nom = 'Peugeot'
        self._km=_km         # _ est indispensable
        self.couleur='Jaune'
        
    def _get_km(self):
        print("Kilométrage en cours" )
        return self._km     # _ est indispensable
    
    def _set_km(self, v):
        print('Mise à jour du kilométrage' )
        self._km = v       # _ est indispensable
    
    prop_km=property(_get_km, _set_km)
    
#%%

Ma_voiture=Voiture(1200)
Ma_voiture.nom
Ma_voiture.prop_km
Ma_voiture.couleur
Ma_voiture._set_km(2000)
Ma_voiture.prop_km=200
Ma_voiture.prop_km

#%% Utilisation des décorateurs
class Voiture1:
    def __init__(self,val_km=0): 
        self.km=val_km
    
    @property 
    def km(self):
        print('Kilométrage au démarrage' )
        return self._km         # _ est indispensable
    
    @km.setter
    def km(self, v):
        print('Mise à jour du kilométrage' )
        self._km = v            # _ est indispensable
        
    @km.deleter
    def km(self):
        print('Remise à zéro du kilométrage' )
        del self._km            # _ est indispensable

#%%

Ma_voiture1=Voiture1(12) # set
Ma_voiture1.km           # get
Ma_voiture1.km=200       # set
Ma_voiture1.km           # get
del(Ma_voiture1.km)      # del
Ma_voiture1.km=200
