"""
Auteur : Samy Hammouti
Date : 22.03.2023
But : tester la fonction affiche_production
"""

from HS_01_affiche_type import *

print("Teste avec une petite liste")
prod= Production("Corse","Validé",196.76)
affiche_production(prod)

lprod = []
for i in range (0,100,1):
    lprod.append(Production("Territoire","statut",i))
affiche_production(lprod)
