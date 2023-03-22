#cree une liste semaine contient les jours

semaine = ["Samedi","Dimache","Lundi","Mardi","Mercredi","Jeudi","Vendredi"]

print ("les jours de la semaine sont:\n", semaine)

print("le valeur de la semaine4 est:\n ",semaine[4])

jour = semaine [0]

semaine[0]= semaine[-1]

semaine[-1]= jour

print (semaine)

print (semaine[6]*12)

for semaine in range (8):
    print(semaine)