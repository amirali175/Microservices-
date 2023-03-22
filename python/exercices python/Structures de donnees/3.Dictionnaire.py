# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:15:04 2022

@author: Amir
"""
# Creer un disctionnaire vide 
contacte = {}

print (contacte) # dictionnaire vide 


''' ajout votre nom et age '''

contacte ["nom"] = "Amir"; # nom est la cle de mon dict et la valeur est amir 
contacte ["age"] = "22 ans"; # age est la cle de mon dict , la valeur est 22 ans 

print ("contacte:", contacte["age"])


""" creer un dictionnaire avec un entier """

dictionnaire1 = {1:10, 2:20, 3:30, 4:40}

print("Mon_dictionnaire1:",dictionnaire1)


       

""" Manipuler les dictionnaires """
                     

""" creer un dictionnaire des jour dans la semaine """

semaine ={1:"Samedi", 2:"Dimanche", 3:"Lundi", 4:"Mardi", 5:"Mercredi", 6:"Jeudi", 7:"Vendredi"};

print (" les jours de la semaine sont :",semaine)

print ("afficher le quartieme jour de la semaine " , semaine [4])

print ("afficher le premiere jour de la semaine " , semaine [1])

# acceder la valeur d'une cle dans les dictionnaires

nom = {}; # un dictionnaire vide 
age = {} ;

nom [0]= "dave"; 
nom [1]= "scare";
nom [2]= "anthony";
nom [3]= "milker";
nom [4]= "raqib";
 
age [0]= "22 ans";
age [1]= "21 ans";
age [2]= "27 ans";
age [3]= "25 ans";
age [4]= "29 ans"

print ("afficher les noms de la dictionnaires:", nom)

#afficher la valeur de la cle 1,3,2

print ("la valeur de la cle 1 est:", nom[0], age[0])

print ("la valeur de la cle 2 est:", nom[1], age[1])

print ("la valeur de la cle 3 est:", nom[3], age[3])

""" Voyons utilser la methode del """

# Supprimer le 2e l'element de votre dictionnaire

del nom [1];
del age [1];

print ("afficher les noms apres la suppression", nom, age)


# Voyons la methode de pop 

""" creer un dictionnaire les mois de l'annee """

dict_mois = {};

dict_mois [1]= "janvier";
dict_mois [2]= "fevrier";
dict_mois [3]= "mars";
dict_mois [4]= "avril";
dict_mois [5]= "mai";
dict_mois [6]= "juine";
dict_mois [7]= "juillet";
dict_mois [8]= "oaut";
dict_mois [9]= "septembre";
dict_mois [10]= "octobre";
dict_mois [11]= "novembre";
dict_mois [12]= "decembre";


#puis afficher le resultat de votre dictionnaire 

print("les mois de l'annnee est:\n", dict_mois)

# ensuite supprimer la 3e l'element de votre dictionnaire 

dict_mois.pop (3);

print("affichage apres la suppression l'element est:\n",dict_mois)



""" Parcourir un dictionnaire """

# Parcourir les cles dictionnaire 

etudiant ={1: " Dave", "ville": "Toronto", "age":22 ,"taille":1.75};

# la maniere le plus simple de parourir un dictionnaire est la boucle for 

for cle in etudiant :
    
    print (cle)
    

# Parcourir les valeur dictionnaire 

# la maniere le plus simple de parourir un dictionnaire est la boucle for 

etudiant ={1: " Dave", "ville": "Toronto", "age":22 ,"taille":1.75};

for valeur in etudiant.values():
    print (valeur )


# utilisons la methode IF dans un dictionnaire 

# creer un dict d'ages des etudiantes college boreal 

etudiants = {"natalie": 27,"fadi": 29, "blevie": 35 };

# afficher l'etudiant le plus age

if 35 in etudiants.values():
    
    print ("un des etudiants est l'age 35")














