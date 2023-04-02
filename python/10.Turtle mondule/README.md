
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
