"""
Auteur : Samy Hammouti
Date : 29.03.2023
But : teste la fonction tranformation.
"""
from HS_02_listes_type import *
from HS_00_type import *
from HS_01_affiche_type import *
print("teste avec une petite liste")
liste = ["territoire","validé","157"]
a = transformation(liste)
print(affiche_liste_production(a))

print("teste avec une grande liste")
l=[]
for i in range (0,100,1):
    l.append(["territoire","statut",i*10])
print(l)
b = transformation(l)
print(affiche_liste_production(b))
