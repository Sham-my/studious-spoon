"""
Aureur : Samy Hammouti
Date : 17/04/2023
But : test de la test de la fonction recherche_dicho_quelconque.
"""
from HS_02_listes_type import*

liste1 = [["","",7],["","",8],["","",8],["","",10],["","",12],["","",13],["","",13],["","",13],["","",13],["","",15],["","",16],["","",16]]
liste1 = transformation(liste1)
liste1 = tri_croissant(liste1)

print("teste avec la valeur la plus petite de la liste")
index7 = recherche_dicho_quelconque (liste1,7)
print(index7,"\n","_"*10)

print("teste avec une valeur qui apparait plusieurs fois")
index13 = recherche_dicho_quelconque (liste1,13)
print(index13,"\n","_"*10)

print("teste avec la valeur la plus grande de la liste")
index16 = recherche_dicho_quelconque (liste1,16)
print(index16,"\n","_"*10)

print("teste avec une valeur qui n'est pas dans liste")
index9 = recherche_dicho_quelconque (liste1,9)
print(index9,"\n","_"*10)
