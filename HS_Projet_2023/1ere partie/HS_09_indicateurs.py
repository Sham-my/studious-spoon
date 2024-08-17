"""
Auteur : Samy Hammouti
date : 12/04/2023
But : teste de toute les fonctions statistiques
"""
from csv import *
from HS_02_listes_type import *
from outils_csv import *



print('teste avec un tableur a 0 lignes.')
liste0 = []
a,LL0 = lecture_fichier("HS_data_TAILLE_0.csv", ";", "utf8", 1)
liste0 = transformation(LL0)
affiche_liste_production(liste0)
print(cout_maximum(liste0),"= cout maximum\n",cout_minimum(liste0),"= cout minimum\n",cout_moyen (liste0),"= cout moyen\n",ecart_type(liste0),"=écart-type")
print("_"*10)



print('teste avec un tableur a 1 lignes.')
liste1 = []
a,LL1 = lecture_fichier("HS_data_TAILLE_1.csv", ";", "utf8", 1)
liste1 = transformation(LL1)
tri_croissant(liste1)
affiche_liste_production(liste1)
print(cout_maximum(liste1),"= cout maximum\n",cout_minimum(liste1),"= cout minimum\n",cout_moyen (liste1),"= cout moyen\n",ecart_type(liste1),"=écart-type\n",mediane(liste1),"=mediane\n",modes(liste1),"=modes")
print("_"*10,"\n")



print('teste avec un tableur a 5 lignes.')
liste5 = []
a,LL5 = lecture_fichier("HS_data_TAILLE_5.csv", ";", "utf8", 1)
liste5 = transformation(LL5)
tri_croissant(liste5)
affiche_liste_production(liste5)
print(cout_maximum(liste5),"=cout maximums\n",cout_minimum(liste5),"=cout minimum\n",cout_moyen (liste5),"= cout moyen\n",ecart_type(liste5),"=écart-type\n",mediane(liste5),"=mediane\n",modes(liste1),"=liste5")
print("_"*10,"\n")


print("teste avec un tableur a 20 lignes.")
liste20 = []
a,LL20 = lecture_fichier("HS_data_TAILLE_20.csv", ";", "utf8", 1)
liste20 = transformation(LL20)
tri_croissant(liste20)
affiche_liste_production(liste20)
print(cout_maximum(liste20),"=cout maximums\n",cout_minimum(liste20),"=cout minimums\n",cout_moyen (liste20),"= cout moyen\n",ecart_type(liste20),"=écart-type\n",mediane(liste20),"=mediane\n",modes(liste20),"=modes")
print("_"*10,"\n")


print('teste avec un tableur a 100 lignes.')
liste100 = []
a,LL100 = lecture_fichier("HS_data_TAILLE_100.csv", ";", "utf8", 1)
liste100 = transformation(LL100)
tri_croissant(liste100)
affiche_liste_production(liste100)
print(cout_maximum(liste100),"=cout maximums\n",cout_minimum(liste100),"=cout minimums\n",cout_moyen (liste100),"= cout moyen\n",ecart_type(liste100),"=écart-type\n",mediane(liste100),"=mediane\n",modes(liste100),"=modes")
print("_"*10,)


