"""
Auteur : Samy Hammouti
Date : 12/04/2023
but : test de la fonction modes
"""

from outils_csv import *
from HS_02_listes_type import*
from csv import *

print("test avec une liste à une valeur.")
liste1 = [["","",3]]
liste1 = transformation(liste1)
frequence1 = modes(liste1)
affiche_liste_production(liste1)
print(frequence1)
print("__"*5)

print("test d'une liste avec un unique mode en début de liste")
liste2 = [["","",4],["","",4],["","",4],["","",6],["","",6],["","",9]]
liste2 = transformation(liste2)
frequence2 = modes(liste2)
affiche_liste_production(liste2)
print(frequence2)
print("__"*5)

print("test d'une liste avec un unique mode ni en début, ni en fin de liste.")
liste3 = [["","",3],["","",4],["","",6],["","",6],["","",9]]
liste3 = transformation(liste3)
frequence3 = modes(liste3)
affiche_liste_production(liste3)
print(frequence3)
print("__"*5)

print("test avec une liste triée contenant plusieurs fois les même valeurs.")
liste4 = [["","",3],["","",3],["","",4],["","",4],["","",6],["","",9],["","",9],["","",9]]
liste4 = transformation(liste4)
affiche_liste_production(liste4)
frequence4 = modes(liste4)
print(frequence4)
print("__"*5)


print("test avec une liste avec plusieurs modes de fréquences non égales à 1.")
liste5 = [["","",3],["","",3],["","",4],["","",4],["","",6],["","",6],["","",6],["","",6],["","",7],["","",7],["","",7],["","",7],["","",9],["","",9],["","",9]]
liste5 = transformation(liste5)
affiche_liste_production(liste5)
frequence5 = modes(liste5)
print(frequence5)
print("__"*5)

