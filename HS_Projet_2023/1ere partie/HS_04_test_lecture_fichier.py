"""
Auteur : Samy Hammouti
date : 24/03/2023
But : teste de la fonction transformation
"""
from csv import *
from HS_02_listes_type import *
from outils_csv import *


print('teste avec un tableur a 0 lignes.')
a,LL0 = lecture_fichier("HS_data_TAILLE_0.csv", ";", "utf8", 1)
liste0 = transformation(LL0)
affiche_liste_production(liste0)
print("Le fichier comtient",len(LL0),"lignes de valeurs et", len(a), "ligne(s) d'entête")
print("_"*10)



print('teste avec un tableur a 1 lignes.')
a,LL1 = lecture_fichier("HS_data_TAILLE_1.csv", ";", "utf8", 1)
liste1 = transformation(LL1)
affiche_liste_production(liste1)
print("Le fichier comtient",len(LL1),"lignes de valeurs et", len(a), "ligne(s) d'entête")
print("__"*10,"\n")



print('teste avec un tableur a 5 lignes.')
a,LL5 = lecture_fichier("HS_data_TAILLE_5.csv", ";", "utf8", 1)
liste5 = transformation(LL5)
affiche_liste_production(liste5)
print("Le fichier comtient",len(LL5),"lignes de valeurs et", len(a), "ligne(s) d'entête")
print("_"*10,"\n")


print("teste avec un tableur a 20 lignes.")
a,LL20 = lecture_fichier("HS_data_TAILLE_20.csv", ";", "utf8", 1)
liste20 = transformation(LL20)
affiche_liste_production(liste20)
print("Le fichier comtient",len(LL20),"lignes de valeurs et", len(a), "ligne(s) d'entête")
print("_"*10,"\n")


print('teste avec un tableur a 100 lignes.')
a,LL100 = lecture_fichier("HS_data_TAILLE_100.csv", ";", "utf8", 1)
liste100 = transformation(LL100)
affiche_liste_production(liste100)
print("Le fichier comtient",len(LL100),"lignes de valeurs et", len(a), "ligne(s) d'entête")
print("_"*10,)

