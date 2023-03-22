
        
QUIZ = { "Qui aimes-tu Amir Ali ": "J'aime Safa"}

for question, reponse_correct in QUIZ:
    reponse = input (f"{question}?")
    
    if reponse == reponse_correct:
        
        print("Cool")

    else:
        print (f"la reponse est {reponse_correct!r}, no pas {reponse!r}")
        
                
    