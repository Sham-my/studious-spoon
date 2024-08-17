"""
Auteur : Samy Hammouti
date : 24/03/2023
But : test de la fonction moyenne
"""
from csv import *
from HS_02_listes_type import *
from outils_csv import *

print("Test avec une liste ordinaire.")
liste5 = []
a,LL5 = lecture_fichier("HS_data_TAILLE_5.csv", ";", "utf8", 1)
liste5 = transformation(LL5)
affiche_liste_production(liste5)
print(cout_moyen(liste5))
print("La moyenne est juste","\n","_"*8,"\n")

print("Test avec une liste ou le cout a toujours la même valeur.")
liste0 = [["","",10],["","",10],["","",10],["","",10],["","",10]]
liste0 = transformation(liste0)
affiche_liste_production(liste0)
print(cout_moyen(liste0))
print("La moyenne est juste","\n","_"*8,"\n")

print("Test avec une liste ou le cout n'a pas toujours la même valeur.")
liste0 = [["","",10],["","",10],["","",10],["","",10],["","",95],["","",34]]
liste0 = transformation(liste0)
affiche_liste_production(liste0)
print(cout_moyen(liste0))
print("La moyenne est juste","\n","_"*8,"\n")

print("la moitié des valeurs valent 2x et l’autre moitié des valeurs vaut 0, ici x faut 5")
liste2 = [["","",10],["","",10],["","",10],["","",0],["","",0],["","",0]]
liste2 = transformation(liste2)
affiche_liste_production(liste2)
print(cout_moyen(liste2))
print("La moyenne est juste","\n","_"*8,"\n")
