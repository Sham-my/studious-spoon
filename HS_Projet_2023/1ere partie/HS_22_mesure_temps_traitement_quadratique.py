"""
Auteur : Samy Hammouti
Date : 26/04/2023
But : Mesure du temps d'un traitement quadratique et les comparer
avec les valeurs d’une fonction de la forme an avec a une constante
"""
import time
from outils_dessin import *
from HS_02_listes_type import *

n = 1000
pas = 10
a = 500
temps_execution_transformation_1 = []
temps_execution_transformation_2 = []
for i in range(pas,n+pas,pas):
    liste = tirage_aleatoire(i)
    tps1 = time.process_time_ns()
    tranfo1 = transformation(liste)
    tps2 = time.process_time_ns()
    temps_execution_transformation_1.append( (i, (tps2-tps1)/1000) )
    
    tps1 = time.process_time_ns()
    for j in range ( 0,a+1,1):
        transfo2 = transformation(liste)
    tps2 = time.process_time_ns()
    temps_execution_transformation_2.append( (i, (tps2-tps1)/1000) )
    
dessine_lignes_brisees(courbe_bleue=temps_execution_transformation_1, 
                       courbe_rouge=temps_execution_transformation_2)


