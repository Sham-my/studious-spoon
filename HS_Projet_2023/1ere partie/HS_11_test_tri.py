"""
Auteur : Samy Hammouti
date : 06/04/2023
But : teste de la fonction tri_croissant.
"""
from csv import *
from HS_02_listes_type import *
from outils_csv import *


print("teste avec une liste de taille 20 non triée.")
liste20 = []
a,LL20 = lecture_fichier("HS_data_TAILLE_20.csv", ";", "utf8", 1)
liste20 = transformation(LL20)
affiche_liste_production( liste20 )
print("_______________")
tri_croissant(liste20)
affiche_liste_production( liste20 )
print("___"*8,"\n")

print("teste avec une liste de taille 19 non triée")
liste19 = []
a,LL19 = lecture_fichier("HS_data_TAILLE_19.csv", ";", "utf8", 1)
liste19 = transformation(LL19)
affiche_liste_production(liste19)
print("_______________")
tri_croissant(liste19)
affiche_liste_production(liste19)

print("___"*8,"\n")

