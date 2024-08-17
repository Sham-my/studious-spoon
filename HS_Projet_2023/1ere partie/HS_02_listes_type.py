"""
Auteur : Samy Hammouti
Date : 22.03.2023
But : contenir toutes les fonctions de manipulation d’une
liste de ptoduction d'électricité.
"""

from HS_01_affiche_type import *
from random import randint

def affiche_liste_production( lprod ) :
    """
    donnée : lprod : liste de valeur de type Production
    Rôle : affiche la liste des informations de production
    """
    if lprod == [] :
        print("Aucune valeur")
    else :
        for i in range (0,len(lprod),1):
            affiche_production(lprod[i])
            
def transformation(LL):
    """
    donnée : LL : liste de listes de chaine de caractères
    précondition :
        - LL ne contient que des données sur des productions.
        - Le nom du territoire est à l'indice 1, le statut est à l'indice 2
            et le cout moyen de production est à l'indice 3.
        Résultat : liste de valeur de type Production
        Rôle : transformation de listes
        """
            
    lprod=[]
    for i in range (0,len(LL),1):
        liste=[]
        for j in range (0,len(LL[i]),1):
            liste.append(LL[i][j])
        prod = Production(liste[0],liste[1],float(liste[2]))
        lprod.append(prod)
    return lprod

def cout_minimum (LL):
    """
    donnée : LL : liste de valeur de type Production.
    Précondition : la variable cout doit être de type float.  
    Rôle : renvoyer la valeur la plus petite de type cout.
    """
    if LL == []:
        cout_min = "liste vide"
    else :
        cout_min = LL[0].cout
        for i in range (0,len(LL),1):
            if cout_min > LL[i].cout :
                cout_min = LL[i].cout
    return cout_min

def cout_maximum (LL):
    """
    donnée : LL : liste de valeur de type Production.
    Précondition : la variable cout doit être de type float.  
    Rôle : renvoyer la valeur la plus grande de type cout.
    """
    if LL == []:
        print("liste vide")
        cout_max = 0
    else:
        cout_max = LL[0].cout
        for i in range (0,len(LL),1):
            if cout_max < LL[i].cout :
                cout_max = LL[i].cout
    return cout_max

def cout_moyen (LL):
    """
    donnée : LL : liste de valeur de type Production.
    Précondition : la variable cout doit être de type float.  
    Rôle : renvoyer la moyenne de type cout.
    """
    if LL != []:
        somme = 0
        for i in range(0,len(LL),1):
            somme += LL[i].cout
        moyenne = somme/len(LL)
        return moyenne
    else:
        return "liste vide"

def ecart_type(LL):
    """
    donnée : LL : liste de valeur de type Production.
    Précondition : la variable cout doit être de type float.  
    Rôle : renvoyer l'écart-type de type cout.
    """
    if LL != []:
        sommes = 0
        moyenne = cout_moyen (LL)
        for i in range (0,len(LL),1):
            sommes += (LL[i].cout)**2
        ecart_type = ((1/len(LL)*sommes)-moyenne**2)**0.5
        return ecart_type
    else:
        return "liste vide"

def verif_tri_croissant(LL):
    """
    donnée : LL : liste de valeur de type Production.
    Précondition : la variable cout doit être de type float.  
    Rôle : Déterminer si la liste est triée.
    """
   
    not_tri = 0
    if len(LL) == 0:
        return print(("Liste vide."))
    elif len(LL) > 0:
        index = LL[0].cout
        for i in range(1,len(LL),1) :
            if index <= LL[i].cout :
                index = LL[i].cout
            elif index > LL[i].cout:
                not_tri+=1
    if not_tri>0:
        return print("La liste n'est pas triée par ordre croissant.")
    else :
        return print("La liste est trier par ordre croissant.")


def tri_croissant(LL):
    """
    donnée : LL : liste de valeur de type Production.
    Précondition : la la liste ne doit pas etre vide.  
    Rôle : trier la liste par ordre croissant.
    """
    liste_triee = [] 
    for i in range (0,len(LL)-1,1):
        indice_mini = i
        for j in range (i+1,len(LL),1):
            if LL[j].cout < LL[indice_mini].cout:
                indice_mini = j
                
        LL[indice_mini],LL[i] = LL[i], LL[indice_mini]
    return LL

def mediane(LL) :
    """
    donnée : LL : liste de valeur de type Production.
    Précondition : la la liste ne doit pas etre vide et triée la liste par ordre croissant .  
    Rôle : renvoie la mediane.
    """
    mid = len(LL)//2-1
    if len(LL)%2 == 0:
        mediane = (LL[mid].cout + LL[mid+1].cout)/2
        return mediane
    else:
        mediane = LL[mid+1].cout
        return mediane


def modalite(LL):
    """
    donnée : LL : liste de valeur de type Production.
    Précondition : la liste ne doit pas être vide et la liste doit etre trié par ordre croissant.  
    Rôle : renvoie les modalités.
    """
    base = LL[0].cout
    modalite=[base]
    for i in range (1,len(LL),1) :
        if LL[i].cout != base:
            modalite.append(LL[i].cout)
            base = LL[i].cout
    return modalite


def modes(LL):
    """
    Donnée : LL : liste de valeur de type Production.
    Précondition : la liste ne doit pas être vide et la liste doit être trié par ordre croissant.  
    Rôle : renvoie la valeur la plus frequente.
    Information : index renvoie au positionnement de la premère valeur de la mode dans la liste
    """
    modal = modalite(LL)
    frequence = 0
    liste_frequence=[]
    index = 0
    for i in range (0,len(LL),1):
        if modal[index] == LL[i].cout:
            frequence += 1
        else :
            liste_frequence.append(frequence)
            frequence = 1
            index += 1
    liste_frequence.append(frequence)

    return liste_frequence

def recherche_dicho_quelconque (liste,v):
    """
    Donnée : liste : liste de valeur de type Production.
                 v : la valeur que l'on cherche.
    Précondition : liste non vide et rangée en ordre croissant.
    Rôle : recherche une valeur dans une liste avec une complexité logarithmique.
    Résultat : Renvoie l'indice de la valeur recherché.
    """
    debut = 0
    fin = len(liste)-1
    while debut <= fin :
        milieu = (debut + fin)//2
        if v == liste[milieu].cout:
            return milieu
        if v > liste[milieu].cout:
            debut = milieu+1
        else:
            fin = milieu-1
    return-1

def recherche_dicho_plus_petit_indice (liste,v):
    """
    Donnée : liste : liste de valeur de type Production.
                 v : la valeur que l'on cherche.
    Précondition : liste non vide et rangée en ordre croissant.
    Rôle : recherche l'indice le plus petit d'une valeur dans une liste avec une complexité logarithmique.
    Résultat : Renvoie l'indice le plus petit de la valeur recherché.
    """
    debut = 0
    fin = len(liste)-1
    pos = -1
    while (debut <= fin):
        mid = (fin + debut)//2
        if liste[mid].cout == v:
            pos = mid
            fin = mid-1
        else:
            if v < liste[mid].cout:
                fin = mid-1
            else:
                debut = mid+1
    return pos


def recherche_dicho_plus_grand_indice (liste,v):
    """
    Donnée : liste : liste de valeur de type Production.
                 v : la valeur que l'on cherche.
    Précondition : liste non vide et rangée en ordre croissant.
    Rôle : recherche l'indice le plus grand d'une valeur dans une liste avec une complexité logarithmique.
    Résultat : Renvoie l'indice le plus grand de la valeur recherché.
    """
    debut = 0
    fin = len(liste)-1
    pos = -1
    while (debut <= fin):
        mid = (fin+debut)//2
        if liste[mid].cout == v:
            pos = mid
            debut = mid+1
        else:
            if v < liste[mid].cout:
                fin = mid-1
            else:
                debut = mid+1
    return pos


def nombres_occurrences(liste,v):
    """
    Donnée : liste : liste de valeur de type Production.
                 v : la valeur que l'on cherche.
    Précondition : liste non vide et rangée en ordre croissant.
    Rôle : déterminer en temps logarithmique, le nombre d’éléments dans une liste
    dont l’attribut att_num a une valeur égale à celle fournie en paramètre.
    Résultat : Renvoie le nombre d'éléments dans la liste égal a la valeur recherché.
    """
    index_min = recherche_dicho_plus_petit_indice (liste,v)
    index_max = recherche_dicho_plus_grand_indice (liste,v)
    occurences = index_max-index_min+1
    return occurences


def tirage_aleatoire_type_production(n):
    """
    Donnée : liste : liste de valeur de type Production.
                 n : longeur de la liste aléatoire. 
    Rôle : tirer aléatoirement une liste de valeurs de type cout.
    Précondition : n doit être supérieure a 0 et la liste ne doit pas être vide.     
    Résultat : Renvoie une liste de valeur cout desorganiser.
    """
    liste_aleatoire = []
    for i in range (0,n,1):
        liste_aleatoire.append(Production("fictif",'statut',n*i))
    return liste_aleatoire


    
def tirage_aleatoire(n):
    """
    Donnée :  n : longeur de la liste aléatoire. 
    Rôle : tirer aléatoirement une liste de valeurs de type cout.
    Précondition : n doit être supérieure a 0 et la liste ne doit pas être vide.     
    Résultat : Renvoie une liste de valeur cout desorganiser.
    """
    liste_aleatoire = []
    for i in range (0,n,1):
        liste_aleatoire.append(["fictif",'statut',randint(100,1000)])
    return liste_aleatoire
