# Exercices: une liste de chaine de caractere

#Creer une liste des 10 noms de fruit de mer et affiche le resultats ?
#et quel type de variables utilise ?
#(choisissez les noms de fruit de mer que vous voulez )

fruit_mer = [ 'huîtres', 'moules', 'coquille saint-jacques', 'pétoncles',
              'clams', 'palourdes', 'coque', 'amande', 'telline', 'praire']
print(fruit_mer)

#Affichez troisieme element a votre liste de fruit de mer ?

print(fruit_mer[3])

#  Affichez huitieme element a votre liste de fruit de mer ?

print(fruit_mer [7])

# Maintenant declarer les elements de la troisieme au cinquieme de la liste ?

print(fruit_mer [2:5])

# Exercice une liste de nombres

#Inventer d'une liste de nombre 0 a 9 afficher le resultat ?

numero = [0,1,2,3,4,5,6,7,9]
print(numero)

# Afficher le deuxieme puis cinquieme nombres de votre liste ?

print(numero[:2])
print(numero[:5])

# Dit nous le sixieme elements de notre liste de nombre

print(numero[:6])

# Exercice une liste contenir d'autre liste

#Dans cet exercice nous melangons deux variable
#(une chaine de caracterer et le nombre ) dans une autre liste nommer maliste et afficher le resultat ?

chaines = ['farxia', 'zeinab', 'yasmin']

nombres = [1,2,3,4]

maliste = [chaines ,nombres ]
print(maliste)

# Exercice : Ajouter des elements a une liste

#  Ajouter des elements la liste de votre fruits de mer ?

fruit_mer.append("rot d'ours")
fruit_mer.append('ami')
print(fruit_mer)


