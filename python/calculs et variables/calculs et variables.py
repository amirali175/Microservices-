
#Combien de pieces aurais-tu dans ton coffre a tresor
#si tu faisais cela pendant un an ?
pieces_trouves = 20
pieces_magic = 10
annee = 365
totale = ((annee* pieces_magic) + pieces_trouves )
print(totale)

#Et maintenant que se passe-t-il si un corbeau decouvre ton tresor et
# entre chaque semaine dans ta chambre pour voler 3 pieces ?
#Au bout d'une annee de ce jeu-la , combien te resterait-il de pieces ?


semaines = 52
pieces_vole = 3
pices_possede = 3670
totale = ( pices_possede- (pieces_vole*semaines))
print (totale)

# que se passerait-il si tu placais un epouvantail devant ta fenetre
# si le corbeau ne pouvait plus voler que deux pices au lieu de trois ?
# chaque fois un coup de pied dans la machine a dupliquer de ton grand-pere
# et si elle produit chaque jour 3 pieces de plus ,
# combien de pieces obtiendras-tu a la fin de l'annee ?

pieces_vole = 2
pieces_trouves = 20
pieces_magic = 13
annee = 365
semaines = 52
totale = ((annee* pieces_magic) + pieces_trouves - (semaines * pieces_vole))

print(totale)






