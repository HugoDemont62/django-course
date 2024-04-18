# -*- coding: utf-8 -*-

#%% Déclaration d'une fonction
def NomDeLaFonction(parametre1,parametre2,parametre3):
    """ Documentation
    que l'on peut écrire
    sur plusieurs lignes """	# docstring entouré de 3 guillemets (ou apostrophes)
    #bloc d'instructions		# attention à l''indentation
    resultat=parametre1+parametre2*parametre3
    return resultat

# Utilisation de la fonction
toto=NomDeLaFonction(1,2,3)
print(toto)

# Aide sur la fonction
help(NomDeLaFonction)

#%% Paramètre par défaut
def demo(a, b="deuxième", c="troisième"): 
    """Afficher a, b puis c.""" 
    print(a, b, c) 

# Exemples :
demo("début") # valeur par défaut utilisée pour b et c 
# début deuxième troisième 

demo("début", "milieu") # valeur par défaut utilisée pour c 
# début milieu troisième 

demo("d", "m", "f") # valeur par défaut non utilisées 
#d m f 
demo("d", c="f") # valeur par défaut utilisée pour b 
# d deuxième f 

#%% Portée des variables

# Variable locale
a = 10		# variable globale au programme
def MaFonction():
    a = 20	# variable locale à la fonction
    print(a)
    return
print(a)		# nous sommes dans l'espace global du programme
#10
MaFonction()	# nous sommes dans l'espace local de la fonction
#20
print(a)		# retour dans l'espace global
#10

# Variable globale
a = 10		# variable globale
def MaFonction():
    global a	# la variable est maintenant globale
    a = 20
    print(a)
    return

print(a)
#10
MaFonction()
#20
print(a)
#20
    
#%% Fonction lambda
def f(x): 
    return x*2 
f(3) 
# 6
# Ex1: 
g = lambda x: x*2
g(3) 
# 6 

# Ex2:
(lambda x: x*2)(3)

plus=lambda x,y:x+y
plus(2,3)
