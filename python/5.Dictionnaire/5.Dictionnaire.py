# Cet exercices nous allons decouvrer comme les autres lecons le dictionnaire

# prenons de personnes et de leurs sports favoris tapez ces informations dans
# une liste , avec le nom de chaque personne suive de son sport favori ?
# le noms et le sport favoris est ci-dessous

sports_favoris = ['Ralph Williams, Football', 'Michael Tippett, Basket-ball',
                  'Edward Elgar, Base-ball', 'Rebecca Clarke, Volley-ball',
                  'Ethel Smyth, Badminton', 'Frank Bridge, Rugby']
print(sports_favoris)

# Quel est le sport preferer de Rabecca Clarke ?
print(sports_favoris[3])

# A present, stockons ces informations dans un dictionnaire,
# avec le nom de personne comme cle et son sport prefere comme valeur.

sports_favoris = sports_favoris = {'Ralph Williams':'Football', 'Michael Tippett': 'Basket-ball',
                                   'Edward Elgar':'Base-ball', 'Rebecca Clarke': 'Volley-ball',
                                   'Ethel Smyth': 'Badminton', 'Frank Bridge': 'Rugby'}
print(sports_favoris['Rebecca Clarke'])

# Supprimer la valeur Ethel Smyth dans le dictionnaire ?
# et quel fonction utilisez-vous ?

del sports_favoris ['Ethel Smyth'] # FONCTION DEL 
print(sports_favoris)

#Remplacer le sport favoris de fotball par Hockey sur glace ,
# a partir de la cle Ralph Williams ?

sports_favoris['Ralph Williams'] = 'football'
print(sports_favoris)



