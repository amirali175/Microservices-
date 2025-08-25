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

Docker vérifie si l'image hello-world est disponible localement.
Si ce n'est pas le cas, il télécharge automatiquement (ou "pull") l'image depuis Docker Hub.
Docker crée un nouveau conteneur basé sur cette image.
Le conteneur s'exécute, affiche un message, puis se termine.
Maintenant que nous avons exécuté notre premier conteneur, explorons plus en détail les images Docker. Rappelez-vous, une image est comme un plan ou un modèle pour un conteneur. Elle contient toutes les instructions nécessaires pour créer un conteneur.

Pour voir les images disponibles sur votre système local, utilisez la commande suivante :

```

```

