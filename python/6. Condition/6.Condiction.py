# instruture if une condition superieur (la signe (>))


age = 13
if age > 20:
    print('tu es trop vieux!')

age = 25
if age > 20:
    print('tu es trop vieux!')
    print('que fais-tu par la ')

# une condition d'egalite (signe (==))

age = 10
if age == 10:
    print("Qu'est ce-que une chauve-souris avec un perruque ? " )
    print('un souris!')

#Dont la  condition if permet seulement afficher le resultat lorsque la condition
# est vrai le message peut s'afficher l'ecran

# Instruction if et elif nous utilison le condiction egalite
age = 27
if age ==26:
     print('comment appellez-vous?')
     print('j\'appelle Bahar!')
elif age == 22:
    print('comment appellez-vous?')
    print('j\'appelle Chamark!')
elif age == 20:
    print('comment appellez-vous?')
    print('j\'appelle Chamark!')

elif age == 27:
    print('comment appellez-vous?')
    print('j\'appelle Amir!')

else :
    print('pardon')

# Instruction if et elif condiction supeurieur
note = 19
if note > 15:
    print("Tres-bien" )
elif note > 14:
    print("Bien")
elif note > 12:
    print('Assez-Bien')
elif note >20:
    print("Genial")

# Combiner des condition
age = 55
if age == 10 or age == 11 or age == 12:
    print("Quel ages-vous ? ")
    print("Mon ages est 55 ans")
else:
    print('pardon')
# equipe de france national

#1.Barre de chocolatees

#Creer une instruction if pour verifier que le nombres
#de barres chocolatees dans la variable Barres_choco est plus
#petit que 100 ou plus grand que 500.
#le programme doit afficher (trop peu ou beaucoup trop)
#quand la condition est vraie.

barres_choco = 50
if barres_choco < 100 or barres_choco > 500:
    print('trop peu')
else:
    print("beaucoup trop")


# La somme des nombres

a = 7
b = 5

la_somme = (a+b)
if la_somme == 11:
    print("la somme de la resulat  n'est pas correcte   ")
else:
    print("Essayer de trouve le bon resulat encore faire des efforts ")
if la_somme  ==12:
    print('la resultat de la somme est' ,la_somme)

#Difference entre nombres et chaines

age = 27
print(age)






