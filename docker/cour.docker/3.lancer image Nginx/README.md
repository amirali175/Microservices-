# 😋Introduction


Dans cet atelier, nous explorerons les images Docker, qui constituent la base de la création et de l'exécution de conteneurs. Nous apprendrons à extraire des images de Docker Hub, à exécuter des conteneurs avec différentes versions d'images, à lister et supprimer des images, à comprendre les calques d'images, à rechercher des images et à effectuer un balisage d'images de base. Cette expérience pratique vous permettra d'acquérir les compétences essentielles pour travailler efficacement avec les images Docker. Si vous débutez avec Docker, pas d'inquiétude : nous vous guiderons pas à pas avec des explications détaillées.

◼️ NGINX
-----------

Nginx, prononcé comme « engine-ex », est un serveur web open-source qui, depuis son succès initial en tant que serveur web, est maintenant aussi utilisé comme reverse proxy, cache HTTP, et load balancer.

Premiere Partie:Telecharger nginx
---------------------------------

Maintenant, récupérons l'image Nginx. Saisissez la commande suivante et appuyez sur Entrée : 
```
$docker pull nginx
```
Cette commande indique à Docker de télécharger la dernière version de l'image Nginx depuis Docker Hub.

Maintenant que nous avons téléchargé l'image, vérifions qu'elle est bien présente sur notre système. Pour cela, nous listons toutes les images que Docker possède localement :
```
$docker images
```


Exercice de rechauffement 
------------------------
Exécution de différentes versions d'une image
Docker vous permet d'exécuter des versions spécifiques d'une image grâce à des balises. Ces balises sont comme des alias pour des versions spécifiques d'une image. Explorons ce concept avec l'image Python.

Commençons par extraire la dernière image Python

Vous obtiendrez un résultat similaire à celui obtenu lors de l'extraction de l'image Nginx. Il s'agit du téléchargement de la dernière version de Python.

Maintenant, extrayons une version spécifique de Python, disons la version 3.7 :


