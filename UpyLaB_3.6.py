Écrire un programme qui imprime la moyenne géométrique \sqrt{a.b} (la racine carrée du produit de a par b) de deux nombres positifs a et b de type float lus en entrée.

Si au moins un de ces nombres est strictement négatif, le programme imprime le mot Erreur.


Réponse :
a = float(input())
b = float(input())

if 0 > a or 0 > b :
    print("Erreur")
else :
    moy = (a * b) ** 0.5
    print(moy)
