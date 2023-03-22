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

