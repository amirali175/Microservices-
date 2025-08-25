# ⚓ Executer Votre Premier Conteneur.

Maintenant que nous comprenons les concepts de base, exécutons notre premier conteneur Docker en utilisant l'image hello-world. Cette simple image est conçue pour vérifier que votre installation de Docker fonctionne correctement et pour vous initier aux bases de Docker.

```
docker run hello-world
```


🃏Analysons ce que cette commande fait :
------------------------------------------

◾docker : C'est la commande pour interagir avec le Docker Engine.

◾run : Cette sous-commande indique à Docker de créer et de démarrer un nouveau conteneur.

◾hello-world : C'est le nom de l'image que nous voulons exécuter.

Lorsque vous exécutez cette commande, plusieurs choses se passent en coulisse :

1.Docker vérifie si l'image hello-world est disponible localement.

2.Si ce n'est pas le cas, il télécharge automatiquement (ou "pull") l'image depuis Docker Hub.

3.Docker crée un nouveau conteneur basé sur cette image.

4.Le conteneur s'exécute, affiche un message, puis se termine.

Maintenant que nous avons exécuté notre premier conteneur, explorons plus en détail les images Docker. Rappelez-vous, une image est comme un plan ou un modèle pour un conteneur. Elle contient toutes les instructions nécessaires pour créer un conteneur.

Pour voir les images disponibles sur votre système local, utilisez la commande suivante :

```
docker images
```

Résumé
------
Félicitations! Vous avez terminé votre premier laboratoire Docker et avez franchi les premières étapes dans le monde de la conteneurisation! Vous avez appris à :

Comprendre les concepts de base de Docker

Exécuter votre premier conteneur en utilisant l'image hello-world

Afficher et comprendre les images Docker sur votre système

Naviguer sur Docker Hub pour trouver et en savoir plus sur les images

Ce n'est que le début de votre parcours avec Docker! Vous avez vu à quel point la conteneurisation peut être puissante, même avec des exemples simples. Prêt à faire passer vos compétences au niveau supérieur?

