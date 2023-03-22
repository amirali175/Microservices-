# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 06:08:00 2023

@author: Amir
"""
QUIZ = [("Quel est le pays le plus peuple au monde","la Chine"),
        ("Combien provinces y'a t'il au Canada","12")
        ]

for question,reponse_correct in QUIZ:
    
    question1 = input(f"{question}?")
    
    if question1 == reponse_correct:
        
        print("Coll")
    else:
        
        print(f"la reponse est {reponse_correct!r}, non pas {question1!r}")