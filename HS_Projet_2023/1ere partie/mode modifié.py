from outils_csv import *
from HS_02_listes_type import*
from csv import *



def modes (LL):
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

liste2 = [["","",4],["","",4],["","",4],["","",6],["","",6],["","",9],["","",9]]
liste2 = transformation(liste2)
frequence2 = modes(liste2)
affiche_liste_production(liste2)
print(frequence2)
print("__"*5)
