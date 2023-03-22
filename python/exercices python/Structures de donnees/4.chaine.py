# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 15:52:05 2022

@author: Amir
"""
"""
#Exemple 1 
chaine = "Bonjour tout le monde" # variable a declarer 

print (chaine)# Afficher a le resultat attendu



#creer une chaine de caractere de fruits

fruits = ["pomme de terre ","melons","banane"]


#afficher le resultat 
print(fruits)

# creation de chaine des etudiants 

etudiants = ["David","scare","Anthony","Hassan","Abdullahi"]

print(etudiants)

# ajoutant votre nom dans la liste etudiants 

etudiants.insert(2,"votre_nom") # permet ajouter un object la position de votre choix 

print(etudiants)

# la methode index 

x = fruits.index("melons")

print (x)

# La methode inverse 

fruits.reverse() # permet inverse l'ordre de la liste originale
print(fruits)

etudiants.reverse()
print(etudiants)


#La methode input  sert a laisse que l'utilisateur tapez son variable 

prenoms = input ("veuillez taper votre prenoms: ")

print ("Bonjour",prenoms)


#écrire un programme calculer la somme, multiplication et 
#division deux éléments  a= 30 et b= 10


a = int (input ("a = "))

b = int (input("b = "))

sum = a+b

mul = a*b

div= a/b


print("Sum is", sum)
print("Multiplication is", mul)
print("Division is", div)
"""
"""
print("quelle est votre nom ?\n")

name = input()

print ("Bienvenus",name)
"""

#Écrire un programme pour accepter que l’utilisateur 
#tapez les noms des planètes


planetes = [] # une liste vide 

for i in range(0, 9):

    print("Enter le nom des planetes", i, ":")
    # accept float number from user
    item = str(input())
    # add it to the list
    planetes.append(item)

print("liste des planetes\n:", planetes)








