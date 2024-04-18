# -*- coding: utf-8 -*-

#%% Créer une classe sequence, définit par :
#   -les attributs : chaine et longueur
#   - les méthodes : reverse, complement, reverse complement, frequence


#%% définition de la classe sequence
class sequence:
    """
    Un exemple de classe :
    opérations de base sur une séquence
    """
    # définition de la méthode spéciale __init__ (constructeur)
    def __init__(self,chaine,longueur):
        self.chaine = chaine.upper()
        self.longueur = longueur
 
    # définition de la méthode reverse
    def reverse(self,chaine):
        return chaine[::-1]
    
    # définition de la méthode complement
    def complement(self):
        self.comp = self.chaine.lower()
        self.comp = self.comp.replace('a','T')
        self.comp = self.comp.replace('t','A')
        self.comp = self.comp.replace('c','G')
        self.comp = self.comp.replace('g','C')
        return self.comp

    # définition de la méthode reverse_complement
    def reverseComplement(self):
        self.revComp = self.complement()
        self.revComp =self.reverse(self.revComp)
        return self.revComp

    # définition de la méthode frequence 
    def frequence(self):
        pA = self.chaine.count('A')/len(self.chaine)
        pT = self.chaine.count('T')/len(self.chaine)
        pC = self.chaine.count('C')/len(self.chaine)
        pG = self.chaine.count('G')/len(self.chaine)       
        return {"A":pA,"T":pT,"C":pC,"G":pG}
        
    
    
seq = sequence("ATCGAATTCGGA", 12)
print(seq.complement())
print(seq.reverseComplement())