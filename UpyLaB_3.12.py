Carré de X,
Cet exercice propose une variante de l’exercice précédent sur le carré de X.

Écrire un programme qui lit en entrée une valeur naturelle n et qui affiche à l’écran un triangle supérieur droit formé de X (voir exemples plus bas).

Exemple 1
Avec la donnée lue suivante :

6
le résultat à imprimer vaudra :

XXXXXX
 XXXXX
  XXXX
   XXX
    XX
     X


réponse 

N = int(input())
i = 0
V = 0

while N > 0:
    for i in range(N) :
        print(V * " " + N * "X")
        N = N - 1
        V = V + 1
print()
