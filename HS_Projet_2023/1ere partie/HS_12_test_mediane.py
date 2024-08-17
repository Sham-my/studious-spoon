
"""
Auteur : Samy Hammouti
Date : 12/04/2023
but : test de la fonction mediane
"""

from outils_csv import *
from HS_02_listes_type import*


print('teste avec un tableur a 1 lignes.')
liste1 = []
a,LL1 = lecture_fichier("HS_data_TAILLE_1.csv", ";", "utf8", 1)
liste1 = transformation(LL1)
print(mediane (liste1),"= mediane")
print("_"*10,"\n")

print("teste avec un tableur a 20 lignes.")
liste20 = []
a,LL20 = lecture_fichier("HS_data_TAILLE_20.csv", ";", "utf8", 1)
liste20 = transformation(LL20)
liste20 = tri_croissant(liste20)
affiche_liste_production(liste20)
print(mediane (liste20),"= mediane")
print("_"*10,)


print("test avec un tableur avec un nombre de ligne impaire")
liste15=[]
for i in range (0,15,1):
    liste15.append(liste20[i])
affiche_liste_production(liste15)
print(mediane (liste15),"= mediane")
print("_"*10,)

    
print("teste avec un tableur a 100 lignes.")
liste100 = []
a,LL100 = lecture_fichier("HS_data_TAILLE_100.csv", ";", "utf8", 1)
liste100 = transformation(LL100)
liste20 = tri_croissant(liste100)
print(mediane (liste100),"= mediane")
print("_"*10,)

print("Après vérification sur exel toutes les médianes sont juste.")

