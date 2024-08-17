"""
Aureur : Samy Hammouti
Date : 17/04/2023
But : test de la test de la fonction nombres_occurrences.
"""

from HS_02_listes_type import*

liste1 = [["","",7],["","",8],["","",8],["","",10],["","",12],["","",13],["","",13],["","",13],["","",13],["","",15],["","",16],["","",16]]
liste1 = transformation(liste1)

print("teste avec la valeur 7 la plus petite de la liste, qui apparait une fois.")
valeur7 = nombres_occurrences(liste1,7)
print(valeur7,"\n","_"*10)

print("teste avec la valeur 13 qui apparait 4 fois")
valeur13 = nombres_occurrences(liste1,13)
print(valeur13,"\n","_"*10)

print("teste avec la valeur 16 la plus grande de la liste qui apparait 2 fois.")
valeur16 = nombres_occurrences(liste1,16)
print(valeur16,"\n","_"*10)

print("teste avec une valeur qui n'est pas dans liste")
valeur9 = nombres_occurrences(liste1,9)
print(valeur9,"\n","_"*10)
