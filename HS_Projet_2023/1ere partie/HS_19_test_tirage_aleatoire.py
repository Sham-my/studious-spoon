"""
Auteur : Samy Hammouti
Date : 25/04/2023
But : teste de la fonction tirage_aleatoire_type_production et tirage_aleatoire.
"""
from HS_02_listes_type import *

print("teste de la fonction 'tirage_aleatoire_type_production'\nteste avec n égual a 50 :")
liste = tirage_aleatoire_type_production(50)
affiche_liste_production(liste)
print("__"*10)

print("teste avec n égual a 0 :")
liste1 = tirage_aleatoire_type_production(0)
affiche_liste_production(liste1)
print("__"*10)

print("teste avec n égual a 500 :")
liste2 = tirage_aleatoire_type_production(500)
affiche_liste_production(liste2)
print("____"*10)


print("teste de la fonction 'tirage_aleatoire'\nteste avec n égual a 50 :")
liste = tirage_aleatoire(50)
print(liste)
print("__"*10)

print("teste avec n égual a 0 :")
liste1 = tirage_aleatoire(0)
print(liste1)
print("__"*10)

print("teste avec n égual a 500 :")
liste2 = tirage_aleatoire(500)
print(liste2)
print("__"*10)
