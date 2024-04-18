# -*- coding: utf-8 -*-

#%%
#import sys
#sys.path.append('C:\\Users\\Formateur\\Desktop\\Exo jour3')
# Ces lignes ne sont à exécuter qu'une seule fois pour ajouter le chemin d'accès au module
# Classesequence_solution
#%%
from Classesequence_solution import sequence

dna = 'gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctggg'



seq = sequence(dna)
#print(seq.chaine())
print(seq.reverse())
#print(seq.complement())
print(seq.reverse_complement())
print(seq.frequence())
print(seq.chaine)