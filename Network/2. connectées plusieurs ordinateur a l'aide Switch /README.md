# 🔖 Reseaux local (LAN)

🐬. TOPOLOGIE ETOILE 
-----------------------

🥷 Scenario mis en place
--------------------------

un entreprise qui a ouvrir ses portes veut installer un reseau local elle dispose 10 equpements (un server DHCP,EMAIL,DNS) et aussi des ordinateur.
Le nom de l'entreprise Xcamp

🍡  architecture Xcamp
--------------------------

![image](https://github.com/amirali175/Microservices-/assets/54910751/329ed32e-82f0-4fed-95f0-5b13ffaf9ec4)


⁉️:Problematique de reseaux 
----------------------------
◼️:Domaine de collision
----------------------
Un domaine de collision est un ensemble d’entités (cartes réseaux) qui partagent le même média de communication. Prenons un exemple dans la vraie vie:

4 personnes utilisent chacun un talkie-walkie pour communiquer. Les spécificités du talkie-walkie sont telles qu’une seule personne peut parler à un instant T. Si deux personnes parlent en même temps, les signaux sont corrompus et on ne comprend rien à la communication. On dit alors que ces personnes sont dans le même domaine de collision.

Dans le monde des réseaux, si deux entités sont dans le même domaine de collision et envoient des données à un instant T alors il y a corruption des données et il faut retransmettre les données.

◼️: repartitionne  les differentes departement a l'aide VLAN
------------------------------------------------------

Un VLAN est un sous-réseau logique de périphériques dans un domaine de diffusion, partitionné par des commutateurs réseau et/ou un logiciel de gestion de réseau, qui peut agir en propre comme un réseau local LAN distinct. Les commutateurs qui prennent en charge les VLAN offrent aux gestionnaires de réseau la possibilité de créer des segments de réseau virtuels flexibles, indépendants de la topologie physique filaire ou sans fil sous-jacente. Les VLAN fonctionnent soit au niveau de la couche de liaison de données Layer 2, soit au niveau de la couche réseau Layer 3, en fonction de la conception du réseau. Différents protocoles réseau prennent en charge les VLAN. C’est le cas notamment de l’Ethernet et du WiFi.

🏴 Configurer correctement un commutateur Cisco signifie que votre réseau peut établir des connexions efficacement. Dans ce guide étape par étape, nous vous expliquons comment configurer les commutateurs Cisco et examinons certaines FAQ.


🌀 Entrez en mode EXEC privilégié et définissez un nom d'hôte pour le commutateur
-----------------------------------------------------------------------------------
```
Switch>enable
Switch#configure terminal
Switch(config)#hostname Switch-central 
```
👼 Attribuez un mot de passe au commutateur
--------------------------------------------
```
Switch-central(config)#enable secret cisco11
```

🏺 Configurer les mots de passe Telnet et d'accès à la console
---------------------------------------------------------------
L'étape suivante consiste à configurer les mots de passe pour Telnet et l'accès à la console. La configuration des mots de passe pour ceux-ci est importante car elle rend votre commutateur plus sécurisé. Si quelqu'un sans autorisation obtient un accès telnet, cela met votre réseau en danger. Vous pouvez configurer des mots de passe en saisissant les lignes suivantes (voir le paragraphe du haut pour Telnet et le paragraphe du bas pour l'accès à la console).


```
Switch-central(config)#line vty  0 15
Switch-central(config-line)#password Terminal@12
Switch-central(config-line)#login 
Switch-central(config-line)#exit
```
🧮 Configure Vlan via interface ports 
-------------------------------------
◾ attribue le vlan 10 les ports interface 0/1 a 0/8
```
Switch-central(config)#interface range fastEthernet 0/1-8
Switch-central(config-if-range)#switchport mode access 
Switch-central(config-if-range)#vlan 10
Switch-central(config-vlan)#exit
```
◾ attribue vlan 50 interface 0/10 a 0/15
```
Switch-central(config)#interface range fastEthernet 0/10-15
Switch-central(config-if-range)#switchport mode access 
Switch-central(config-if-range)#vlan 50
Switch-central(config-vlan)#exit
```

◾ attribue vlan 20 interface 0/17 a 0/19
```
Switch-central(config)#interface range fastEthernet 0/17-19
Switch-central(config-if-range)#switchport mode access 
Switch-central(config-if-range)#vlan 20
Switch-central(config-vlan)#exit
```

◾ attribue vlan 30 interface 0/21 a 0/23
```
Switch-central(config)#interface range fastEthernet 0/21-23
Switch-central(config-if-range)#switchport mode access 
Switch-central(config-if-range)#vlan 30
Switch-central(config-vlan)#exit
