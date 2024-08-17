"""
Auteur : Samy Hammouti
Date : 26/04/2023
But : Mesure du temps d'un traitement logarithmique et les comparer
avec les valeurs d’une fonction de la forme an avec a une constante
"""
import time
from outils_dessin import *
from HS_02_listes_type import *
import random 
n = 10000
pas = 100
a = 1000
temps_execution_recherche_dicho_quelconque_1 = []
temps_execution_recherche_dicho_quelconque_2 = []
for i in range(pas,n+pas,pas):
    liste = tirage_aleatoire_type_production(i)
    tps1 = time.process_time_ns()
    dicho1 = recherche_dicho_quelconque(liste,random.randint(pas,n))
    tps2 = time.process_time_ns()
    temps_execution_recherche_dicho_quelconque_1.append( (i, (tps2-tps1)/1000) )
    
    tps1 = time.process_time_ns()
    for j in range ( 0,a+1,1):
        dicho2 = recherche_dicho_quelconque(liste,random.randint(pas,n))
    tps2 = time.process_time_ns()
    temps_execution_recherche_dicho_quelconque_2.append( (i, (tps2-tps1)/1000) )
    
dessine_lignes_brisees(courbe_bleue=temps_execution_recherche_dicho_quelconque_1, 
                       courbe_rouge=temps_execution_recherche_dicho_quelconque_2)

