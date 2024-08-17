"""
Auteur : Samy Hammouti
Date : 12/04/2023
but : tester la fonction maximum
"""
from outils_csv import *
from HS_02_listes_type import*

print('teste avec un tableur a 0 lignes.')
a,LL0 = lecture_fichier("HS_data_TAILLE_0.csv", ";", "utf8", 1)
liste0 = transformation(LL0)
print(cout_maximum (liste0))
print("_"*10)

print('teste avec un tableur a 1 lignes.')
a,LL1 = lecture_fichier("HS_data_TAILLE_1.csv", ";", "utf8", 1)
liste1 = transformation(LL1)
print(cout_maximum (liste1))
print("_"*10,"\n")

print("teste avec un tableur a 20 lignes.")
a,LL20 = lecture_fichier("HS_data_TAILLE_20.csv", ";", "utf8", 1)
liste20 = transformation(LL20)
print(cout_maximum (liste20))
print("_"*10,)

print("teste avec un tableur a 100 lignes.")
a,LL100 = lecture_fichier("HS_data_TAILLE_100.csv", ";", "utf8", 1)
liste100 = transformation(LL100)
print(cout_maximum (liste100))
print("_"*10,)
print("La fonction ne renvoit la valeur maximum après vérification.")
