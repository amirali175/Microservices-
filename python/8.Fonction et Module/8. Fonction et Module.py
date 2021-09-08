def foncttest (mon_nom):
    print("Bonjour %s" % (mon_nom))
foncttest('Amir')

def epargne (argent_poche , petits_boulots, depense ):
    return argent_poche+ petits_boulots-depense
print("les resultat  d'epargne est %s "% epargne(10,10,5))

def test ():
    premiere_variable =10
    seconde_variable =10
    return premiere_variable*seconde_variable
print("le resulat du test est %s "%test())


def construiction_vaisseau (canettes):
    totale_canttes = 0
    for semaine in range (1,53):
        totale_canttes = totale_canttes+ canettes
        print("Semaine %s = %s "% (semaine, totale_canttes))
construiction_vaisseau(2)




import sys
print(sys.stdin.readline())



def age_blague_idiote ( age):
    if age >= 10 and age <= 13:
        print('vous etes adult !')
    else:
        print('Pardon vous n\'est pas admissible')
age_blague_idiote(9)


def age_blague_idiote ():
    print('quel age as-tu ?')
    age = int(sys.stdin.readline())
    if age >=10 and age <= 13:
        print('que donne 13+49')
    else:
        print('pardon?')
age_blague_idiote()

#creer une fonction qui renvoie produit de deux nombres

def produit (x,y):
    return (x*y)
print("le produit de 5 et 7 est ",produit(5,7))

#La sommes de deux nombre

def somme (x,y):
    return (x+y)

print("la somme de 5 et 7 est ",somme(5,7))
