# Tutoriel : Créer et gérer des machines virtuelles Windows avec Azure PowerShell
Les machines virtuelles Azure offrent un environnement informatique entièrement configurable et flexible. Ce tutoriel aborde les tâches de base du déploiement d'une machine virtuelle Azure, comme la sélection de la taille et de l'image de la machine virtuelle, ainsi que son déploiement. Vous apprendrez à :

🃏Créer et se connecter à une VM

🪕Sélectionner et utiliser des images de machines virtuelles

⚓Afficher et utiliser des tailles de machines virtuelles spécifiques

🎱Redimensionner une VM

😠Afficher et comprendre l'état de la machine virtuelle

:one: Lancer Azure Cloud Shell
-----------------------------

![image](image/1.png)

2️⃣ Créer un groupe de ressources
-----------------------------
Créez un groupe de ressources avec la commande New-AzResourceGroup .
```
```

Un groupe de ressources Azure est un conteneur logique dans lequel les ressources Azure sont déployées et gérées. Un groupe de ressources doit être créé avant une machine virtuelle. Dans l'exemple suivant, un groupe de ressources nommé myResourceGroupVM est créé dans la région Est des États-Unis :
