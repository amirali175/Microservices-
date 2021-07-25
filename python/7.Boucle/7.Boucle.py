# Pour afficher 5 fois <<Bonjour>> en python il ya bien cette solution

print("Bonjour")
print("Bonjour")
print("Bonjour")
print("Bonjour")
print("Bonjour")# de repete le meme choses a plusieur fois est assomant

# Pour reduire la repetition et la frappe de clavier on doit utilise la boucle for
for a in range (0,5):
    print(1,"Bonjour")
# Maintenant essayant de compter Bonjour
for x in range (0,5):
    print("Bonjour Amir %s"% x)
    for j in range (0,5) :
        print(j)



pieces_trouvees = 20
pieces_magique = 70
pieces_volees = 3
pieces= pieces_trouvees
for semaine in range (1,53):
    pieces = pieces +pieces_magique -pieces_volees
    print ('Semaine %s = %s'% (semaine,pieces))

for x in range (0,20):
    print('bonjour les filles %s' % x)
    if  x < 9:
        break # Instruction break donnees la possiblite de quitte la boucle au moment où une condition externe est déclenchée

number = 0

for number in range(10):
    if number == 6:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')



import math # pour rendre accessible la librairie mathématique

#------------------- on définit la fonction
def f(t):
    """ Un exemple de fonction faisant appel la la librairie des fonctions
mathématiques : la fonction racine carrée."""
    image=t**2-3*t+2
    return image

#-------------------- le programme principal
"""Le programme va vous demander de choisir en boucle des valeurs de x.
print "Pour sortir, il suffira de choisir la valeur 0."""

 #il faut une valeur différente de 0 pour rentrer dans la boucle
x=2
while(x!=2):
    x=float(input("Rentrer la valeur de x : "))
    if (x<0):
        print("Il faut une valeur positive ou nulle !")
    else :
        resultat=f(x)
        print("f("+repr(x)+ ")="+repr(resultat))
    print("\n")

print("Happy end !")


# -*- coding:utf-8 -*-

print("*** Avant la boucle ***")

entree="bidule"

while entree != "" :
    print("------ dans la boucle ------")
    entree=input("Taper un mot : ")

print("*** Après la boucle ***")
input("Appuyer sur ENTER pour terminer le programme. ")


mot1="Romane"
print(mot1)

mot2="Lucie"
print(mot2)

print("{} et {}".format(mot1,mot2) )


#Nombres Paires

# Cree une boucle quin'affiche que les nombres pairs jusqu'a atteindre ton age ?

x = 20
while x < 30:
    x = x+2
    print(x)

# Mes cinq ingredients preferes
# Cree une liste qui contienne cinq ingrediemnts indispensable pour un bon sandwich
liste_ingredients = ['escargots','sangsues','tranche de gorills',
                     'sourcild de chenilles','orteils de mille-pattes']

for name in liste_ingredients :
    for numero in range(1,5):
        print (numero,name)
