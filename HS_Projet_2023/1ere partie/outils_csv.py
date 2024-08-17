"""
Auteur : G. Richomme
Création 21/01/2023
Contenu : outils de manipulation de fichiers csv
"""
import csv

def lecture_fichier_v1( nom_fichier ):
    """
    Données : nom_fichier : chaîne de caractères
    Précondition : nom_fichier est le nom d'un fichier csv (avec suffixe)
    Résultat : liste de listes de chaîne de caractéres
    Rôle : retour le contenu du fichier nom_fichier
        sous forme d'une liste de listes
    """
    fichier = open(nom_fichier,"r")
    cr = csv.reader(fichier,delimiter=";")

    resultat = []
    for ligne in cr:
        resultat.append( ligne )
    fichier.close()
    return resultat

def lecture_fichier_v2( nom_fichier, separateur, encodage ):
    """
    Données :
        nom_fichier : chaîne de caractères
        separateur : chaîne de caractères
        encodage : chaîne de caractères
    Précondition :
        separateur est de longueur 1
        nom_fichier est le nom d'un fichier csv (avec suffixe)
            dont les séparateur et encodage correspondent aux paramètres
    Résultat : liste de listes de chaîne de caractéres
    Rôle : retourne le contenu du fichier nom_fichier
        sous forme d'une liste de listes
    """
    fichier = open(nom_fichier,"r", encoding=encodage)
    cr = csv.reader(fichier,delimiter=separateur)

    resultat = []
    for ligne in cr:
        resultat.append( ligne )
    fichier.close()
    return resultat

def lecture_fichier( nom_fichier, separateur, encodage, nb_lignes_entete ):
    """
    Données :
        nom_fichier : chaîne de caractères
        separateur : chaîne de caractères
        encodage : chaîne de caractères
        nb_lignes_entete : entier
    Précondition :
        separateur est de longueur 1
        nom_fichier est le nom d'un fichier csv (avec suffixe)
            dont les séparateur et encodage correspondent aux paramètres
        le fichier contient nb_lignes_entete lignes d'en-tête
    Résultat : liste de listes de chaîne de caractéres
    Rôle : retourne le contenu du fichier nom_fichier
        sous forme de deux liste de listes :
        - la première liste de nb_lignes_entete
    """
    fichier = open(nom_fichier,"r", encoding=encodage)
    cr = csv.reader(fichier,delimiter=separateur)

    entete = []
    donnees = []
    compteur = 0
    for ligne in cr:
        if compteur < nb_lignes_entete:
            entete.append( ligne )
        else:
            donnees.append( ligne )
        compteur += 1
    fichier.close()
    return entete, donnees
