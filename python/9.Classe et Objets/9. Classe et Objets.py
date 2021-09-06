# Nous decouvrons dans cette chapitre utilite de classe

#--------------------------------------
#   Nous organisons les choses en classe
#---------------------------------------

# Classe

# Enfant et parent
class chose: # (chose) est le parent des Animes et Inanimes
    pass

# Maintenant Amimes et Inanimes sont les petites enfants de class (chose)

class Animes (chose): #nous créons une classe nommée Inanimes et nous indiquons à Python que sa classe parente est Choses.
    pass

class Inanimes (chose): # c’est au tour de la classe nommée Animes ; nous précisons à Python que sa classe parente est aussi Choses
    pass

class Trottoirs (Inanimes): #nous créons une classe nommée Trottoirs et nous indiquons à Python que sa classe parente est Inanimes.
    pass

#--------------------------------------------------
#Et nous pouvons également établir les classes Animaux,
# Mammiferes et Girafes avec leurs parents respectifs :
#------------------------------------------------------

class Animaux (Animes):
    def respire(self):
        print("respire")
    def bouger (self):
        print("bouge")
    def manger (self):
        print("mange")

class Mammiferes (Animaux):
    def nourir_petit_avec_du_lait(self):
        print("nourrit les petits")



class Girafes (Mammiferes):
    def manger_feuilles_des_arbres(self):
        print("mange des feuilles")

#------------------------------------------------
#            Ajouter des objets aux classes
#--------------------------------------------------

regine = Girafes()
regine.bouger()
regine.manger_feuilles_des_arbres()

jules= Girafes()
jules.bouger ()

#--------------------------------------------
#      Definir des fonction de classes
#---------------------------------------------


def voici_une_fonction_normale():
    print("Je suis une fonction normale.")
voici_une_fonction_normale()



class je_suis_une_classe:
    def voici_une_fonction_classe (self):
        print("Je suis une fonction normale.")
    def voici_une_autre_fonction_classe(self):
        print("Je suis une autre fonction classe Vu?.")




class Girafes (Mammiferes):
    def trouve_nourriture (self):
        self.bouger()
        print("j'ai trouve de la nourriture !")
        self.manger()



# pour creer une classe en python , on utilise l'instruction "class"

#

# je dedies de creer une classe Personne
class personne :
    def __init__(self,nom,age):
        self.nom= nom
        self.age = age
P=personne("Amir",27)
print("le nom de la personne est",P.nom)
print("l'age de la personne est",P.age,'ans')


#cree Rectangle

class Rectangle :
    def __init__(self,L,l):
        self.longeur=L
        self.largeur=l
monrectangle= Rectangle(7,5)
print("la longueur de mon rectangle est",monrectangle.longeur)
print("la largeur de mon rectangle est",monrectangle.largeur)

# ajout de méthode qui calcule la surface du rectangle
class Rectangle :
    def __init__(self,L,l):
        self.longueur=L
        self.largeur=l
    #methode de calcule la surface
    def surface (self):
        return self.longueur*self.largeur
monrectangle=Rectangle(7,5)
print("la surface de mon rectangle est",monrectangle.surface())


#cree un carre
class carre:
    def __init__(self,c):
        self.cote=c
moncote= carre(5)
print("les cotes de mon carre est ",moncote.cote,'cm')

#calculer le perimetre de mon carre

class carre:
    def __init__(self,c):
        self.cote=c
    def perimetre (self):
        return self.cote*4
moncote= carre(5)
print("Le perimetre de la carre est",moncote.perimetre())

#calcule l'aire de carre

class carre :
    def __init__(self,c):
        self.cote=c
        self.cote=c
    def aire (self):
        return self.c*self.c
moncote = carre (5,5)
print ("l'aire de la carre est",moncote.aire())
