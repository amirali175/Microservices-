# 📘 Scenario 


Vous travaillez comme stagiaire dans une grande college et avez acquis la tache de mettre en place VTP (Vlan Trunking Protocol).
Vous devez creer un tas de vlan.

◼️ Buts :

▪️creez les Vlan suivant sur le commutateur Xc :  

▪️Vlan 10 : Nom Eleves.

▪️Vlan 20 : Nom profs.

▪️Vlan : Nom invites.

▪️Configurez les interfaces entre commutateur en tant que jonctions.

▪️Configurez le commutateur "Xc" comme serveur VTP.

▪️Configurez le commutateur "profs" comme un client VTP.

▪️Configurez le commutateur "eleves" comme un client VTP.

▪️Configurez le commutateur profs afin qu'il ne se synchronise pas avec les derniers information VTP, il devrait pas cependant transmettre les publicites au commutateur eleves.

▪️Changez le nom de domaine VTP en "Xcamp11".

▪️Utilisez le mot de passe "Password11" pour VTP.

🌠 Assurez-vous qu'il n'y pas trafic VLAN inutile inonde sur les liaisons principales.

# Je vous souhaite d'avoir Bonne Pratiquer 


## 🥢 Topologie 

![image](https://github.com/amirali175/Microservices-/assets/54910751/6fa5d96a-1118-4f49-bdeb-4367a71a05d2)


◾Mode server sur le commutateur Xc
------------------------------------

C’est le mode par défaut de tous les commutateurs niveau 2 de CISCO. Le commutateur-serveur propage les VLANs et leurs paramètres aux autres commutateurs ‘client’ du même domaine VTP. Le serveur-commutateur enregistre les informations des VLANs dans sa NVRAM. On peut créer, supprimer et renommer les VLANs tout en propageant ces changements aux autres commutateurs du réseau via des paquets ‘vtp advertisement’. Un exemple de la syntaxe de la configuration VTP est :

```
Un exemple de la syntaxe de la configuration VTP est :
Switch(config)#vtp mode server
Device mode already VTP SERVER.
Switch(config)#vtp domain LA_CLASSE
Changing VTP domain name from NULL to LA_CLASSE
```
commande de configuration commutateur Xc 
-----------------------------------------

```

```


