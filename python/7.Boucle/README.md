# 🔖: Presentation des boucles en python 


Les boucles vont nous permettre d’exécuter plusieurs fois un bloc de code, c’est-à-dire d’exécuter un code « en boucle » tant qu’une condition donnée est vérifiée.

Lorsqu’on code, on va en effet souvent devoir exécuter plusieurs fois un même code. Utiliser une boucle nous permet de n’écrire le code qu’on doit exécuter plusieurs fois qu’une seule fois.

Nous allons ainsi pouvoir utiliser les boucles pour parcourir les valeurs d’une variable de liste liste ou pour afficher une suite de nombres.


Nous avons accès à deux boucles en Python :

◾:La boucle while (“tant que…”) ;
◾:La boucle for (“pour…”).

Le fonctionnement général des boucles sera toujours le même : on pose une condition qui sera généralement liée à la valeur d’une variable et on exécute le code de la boucle « en boucle » tant que la condition est vérifiée.

Pour éviter de rester bloqué à l’infini dans une boucle, vous pouvez donc déjà noter qu’il faudra que la condition donnée soit fausse à un moment donné (pour pouvoir sortir de la boucle). Selon le type de condition, on va avoir différents moyens de faire cela. Nous allons voir les plus courants dans la suite de cette leçon.


## :one:La boucle Python while
La boucle while va nous permettre d’exécuter un certain bloc de code « tant qu’une » condition donnée est vrai. Sa syntaxe est la suivante :

Ecrire un programme qui afficher tant que variable x est inferieur a 10   
```
variable x = 0
while variable x < 10 : 
 vriable x = variable x + 1
 
 print (variable x )
 ```
 
## ◼️ exemple : Écrivez un programme pour afficher tous les nombres naturels en sens inverse de n à 1 en utilisant la boucle for et while.
```
n = int (input("saisir un nombre"))
print ( "le nombre nature de {0} a 1".format(n))

for i in range (n,0,-1):
 print (i, "end = ' ')
 
```
```
