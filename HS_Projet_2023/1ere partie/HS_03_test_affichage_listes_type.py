"""
Auteur : Samy Hammouti
Date : 22.03.2023
But : tester la fonction affiche_liste_production
"""
from HS_02_listes_type import *

print("teste avec une petite liste")
lprodu = [Production("Corse","Validé",196.76), Production("Guyane","Validé",313.83)]
affiche_liste_production(lprodu)
print("__"*10)

print("\n teste avec une grande liste")
liste=[]
for i in range (0,100,1):
    liste.append(Production("territoire","Validé",i*10))
affiche_liste_production(liste)
print("__"*10)

print("\n tester avec une liste vide")
prod=[]
affiche_liste_production(prod)

