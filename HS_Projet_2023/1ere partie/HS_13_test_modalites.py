"""
Auteur : Samy Hammouti
Date : 12/04/2023
but : test de la fonction modalite
"""

from outils_csv import *
from HS_02_listes_type import*
from csv import *

print("test avec une liste triée contenant plusieurs fois les même valeurs.")
liste1 = [["","",3],["","",3],["","",4],["","",4],["","",6],["","",9],["","",9]]
liste1 = transformation(liste1)
affiche_liste_production(liste1)
print(modalite(liste1))
print("__"*5)

print("test avec une liste triée contenant que des valeurs différentes.")
liste2 = [["","",3],["","",4],["","",5],["","",6],["","",7]]
liste2 = transformation(liste2)
affiche_liste_production(liste2)
print(modalite(liste2))
print("__"*5)

print("test avec une liste dont tous les éléments sont disctincts")
liste4 = []
for i in range (0,10,1):
    liste4.append(["","",i])
liste4 = transformation(liste4)
tri_croissant(liste4)
affiche_liste_production(liste4)
print(modalite(liste4))
print("__"*5)

print("test avec une liste triée contenant contenants 5 fois la même valeurs de 0 à 10.")
liste5 = []
for i in range (0,5,1):
    for j in range (0,11,1):
        liste5.append(["","",j])
liste5 = transformation(liste5)
tri_croissant(liste5)
affiche_liste_production(liste5)
print(modalite(liste5))
print("__"*5)
