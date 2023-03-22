# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:21:11 2023

@author: Amir
"""

# Premier programme mondule tortue (Turtle)

import turtle 

window = turtle.Screen()
window.setup(500, 500)

mon_turtle = turtle.Turtle() # pour creer un tortue 

mon_turtle.shape("turtle")

mon_turtle.forward(100) # faites bouger la tortue a 100 unites 


mon_turtle.left(90)#changer le sens a 90 degrees 
mon_turtle.forward(100) # faites bouger la tortue a 100 unites


# Exercice 1: creer un carre  

mon_turtle.forward(200)
mon_turtle.left(90)

mon_turtle.forward(200)
mon_turtle.left(90)

mon_turtle.forward(200)
mon_turtle.left(90)

mon_turtle.forward(200)
mon_turtle.left(90)

# utilises la boucle for pour dessiner un carre 

for carre in range(4):
    mon_turtle.forward(100)
    mon_turtle.left(90)
    
    print(carre)
    
    





    
# utiliser la fonction input pour dessiner un carre 

perimaitre = int(input("rentre les messure du cote ?"))

angle = int(input("rentre l'angle du cote ?"))

for carre in range(4):
    mon_turtle.forward(perimaitre)
    mon_turtle.left(angle)

print (carre)