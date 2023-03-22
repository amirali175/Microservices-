# -*- coding: utf-8 -*-
"""
Created on Sat May 14 16:54:17 2022

@author: Amir
"""

# Creer un tuple vide nomme variable

variable = ()

# inclure un elements 50 

variable = (50 );

#Afficher le resulat 

print (variable)


# inventer une tuple avec plusieur element comme la semaine 

semaine = ("Samedi","Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi")

annees = (2000,2001,2002,2003,2004,2005)

#Annoncer le resultat 

print (semaine)

# Dans votre liste de tuple afficher 3e indice de la semaine et l'annees

print (semaine[3]),

print (annees[3]),

# Dans votre liste de tuple afficher 3e et 5e indice de la semaine et l'annees

print (semaine[3:5], annees[3:5]),

# Renverse le tuple de la semaine 

semaine1 = tuple(reversed( semaine))

print (semaine1)

reversed()



