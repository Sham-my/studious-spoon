"""
instructions permettant d’affichage contenue dans le fichier INITIALES_00_type
"""
from HS_00_type import *

def affiche_production(prod):
    """
    donnée : prod : production
    Rôle : afficher les informations sur la production
    """
    print(prod.territoire,":",prod.statut,":",prod.cout,"euro/MWh")
          
