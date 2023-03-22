# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 06:28:53 2023

@author: Amir
"""
"""
# pour creer un diction on utile syntaxe 

dictionnaire = {} # vide

#Pour ajouter des valeurs dans un dictionnaire  faut indiquer une cle aunsi une valeur

dictionnaire ["Nom"] ="Wayne"

dictionnaire ["Prenom"] = "Ali"


for valeur,cle in dictionnaire.items():
    
    question1 = input(f"{valeur}?")
    
    if question1 == cle:
        
        print ("Coll")
        
    else: 
        
        print(f"la reponse est {cle!r}, non pas {question1!r}")
"""       
        
str = " Les joeur du real-madrid"

str.title()

print(str)

joeur = { "numero9":"Benzema","numero10":"Modric","numero11":"Azenzo"}
    
    
    
    
for numero,nom in joeur.items():
    
    question2 = input(f"{numero}?")
    
    if question2 == nom:
        
        print ("super choix")
        
        
    else:
        
        print(f"La reponse est {nom!r}, non pas {question2!r}")
        
        
        
    
QUESTIONS = [ ("Quel est la capitale du Quebec","Quebec-ville"),
             ("Quel est le pays plus peuple au monde","Chine")
             ]

for question,reponse_correct in QUESTIONS:
    reponse =input ("f{question}? ") 
    
    
    if reponse  == reponse_correct:
        
        print ("Correct")
        
    else:
        
        print(f"La reponse est {reponse_correct!r}, no {reponse!r}")
        


       
    
        