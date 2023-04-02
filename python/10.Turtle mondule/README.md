
# 🔖: Turtle Mondule
----------------------

## ◾Premier programme tortue

Introduction : le module tortue est un mode graphique permet a dessiner tracer un courbe geometrique.ce module peut etre un bon outil pour voir le resulats de 
programation.

◾ premier pas: tracer une ligne ou bien un segment 
```
import turtle # importe le module tortue

windows = turtle.Turtle() 

# tracer un sergment 100 unite vers droite et tourne la fliche a gauche 90 degrees
----

turtle.forward (100)
turtle.left(90)

```
◾ Dessiner un carre a l'aide module turtle

```
import turtle 

windows = turtle.Turtle()

window = turtle.Screen()
window.setup(500, 500)

# tracer un sergment 100 unite vers droite et tourne la fliche a gauche 90 degrees

turtle.forward (100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
```
◾ Dessiner un carre a l'aide module turtle avec la boucle for et range 

```
import turtle 

windows = turtle.Turtle()

window = turtle.Screen()
window.setup(500, 500)


for i in range(4):
    
    turtle.forward(100)
    turtle.left(90)
```

◾ Cette fois nous utilissons la fonction input pour dessiner un carre 
```
carre= turtle.Turtle()


PerimaitreAB= int(input('entre la mesure du cote AB:'))

PerimaitreDC= int(input('entre la mesure du cote DC:'))

PerimaitreAC= int(input('entre la mesure du cote AC:'))

PerimaitreBD= int(input('entre la mesure du cote BD:'))


carre.forward(PerimaitreAB)
carre.left(90)
carre.forward(PerimaitreDC)
carre.left(90)



carre.forward(PerimaitreAC)
carre.left(90)
carre.forward(PerimaitreBD)
carre.left(90)
```

## :one: Exercice 1
-------------------

Ecrivez un programation pour dessiner un triangle avec la methode input et boucler for 
```
import turtle

window = turtle.Screen()
window.setup(500, 500)

triangle = triangle.Turtle()
## ecrivez votre programation ici ##
```

