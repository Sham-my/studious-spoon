"""
Auteur :Samy Hammouti
Date : 12/04/2023
but : test de la fonction minimum
"""

from outils_csv import *
from HS_02_listes_type import*

print('teste avec un tableur a 0 lignes.')
liste0 = []
a,LL0 = lecture_fichier("HS_data_TAILLE_0.csv", ";", "utf8", 1)
liste0 = transformation(LL0)
print(cout_minimum (liste0))
print("_"*10)

print('teste avec un tableur a 1 lignes.')
liste1 = []
a,LL1 = lecture_fichier("HS_data_TAILLE_1.csv", ";", "utf8", 1)
liste1 = transformation(LL1)
print(cout_minimum (liste1))
print("_"*10,"\n")

print("teste avec un tableur a 20 lignes.")
liste20 = []
a,LL20 = lecture_fichier("HS_data_TAILLE_20.csv", ";", "utf8", 1)
liste20 = transformation(LL20)
print(cout_minimum (liste20))
print("_"*10,)
print("La fonction ne renvoit la valeur minimum après vérification.")
