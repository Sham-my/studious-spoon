"""
Auteur : Samy Hammouti
Date : 22/03/2023
Type production
"""

class Production( object ):
    def __init__( self, valeur_territoire, valeur_statut, valeur_cout ):
        """
        territoire : chaîne de caractères
        statut : chaîne de caractères
        cout : entier 
        """
        self.territoire = valeur_territoire
        self.statut = valeur_statut
        self.cout = valeur_cout
