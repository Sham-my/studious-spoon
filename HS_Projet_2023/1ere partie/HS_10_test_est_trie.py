"""
Date : 05/04/2023
Auteur : Samy Hammouti
But : tester la fonction verif_tri_croissant.
"""

from csv import *
from HS_02_listes_type import *
from outils_csv import *

print("teste avec une liste vide")
liste0 = []
a,LL0 = lecture_fichier("HS_data_TAILLE_0.csv", ";", "utf8", 1)
liste0 = transformation(LL0)
verif_tri_croissant(liste0)
print("__"*8)

print("teste avec une liste pas triée.")
liste20 = []
a,LL20 = lecture_fichier("HS_data_TAILLE_20.csv", ";", "utf8", 1)
liste20 = transformation(LL20)
verif_tri_croissant(liste20)
print("__"*8)

print("teste avec une liste triée.")
liste20_tri = []
a,LL20_tri = lecture_fichier("HS_data_TAILLE_20_triee.csv", ";", "utf8", 1)
liste20_tri = transformation(LL20_tri)
verif_tri_croissant(liste20_tri)
print("__"*8)
