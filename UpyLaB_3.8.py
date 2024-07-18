
Nom
Volume
Image
Tétraèdre
\frac{\sqrt{2}}{12}a^3
https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/Tetraedre.gif
Cube

a^3
https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/cube.gif
Octaèdre

\frac{\sqrt{2}}{3}a^3
https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/octaedre.gif
Dodécaèdre

\frac{15 + 7\sqrt{5}}{4}a^3
https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/dodecaedre.gif
Icosaèdre

\frac{5(3 + \sqrt{5})}{12}a^3

Écrire un programme qui lit :

la première lettre en majuscule du nom du polyèdre ("T", "C", "O", "D" ou "I"),

la longueur de l’arête du polyèdre,

et qui imprime le volume du polyèdre correspondant.

Si la lettre lue ne fait pas partie des cinq initiales, le programme imprime le message "Polyèdre non connu".

Exemple 1
Avec les données lues suivantes :

C
2.0
le résultat à imprimer vaudra :

8.0
Exemple 2
Avec les données lues suivantes :

I
2.0
le résultat à imprimer vaudra (approximativement) :

17.4535599249993
Exemple 3
Avec les données lues suivantes :

A
2.0
le résultat à imprimer vaudra :

Polyèdre non connu

Réponse 
import math
polye = str(input())
a = float(input())

if polye == "T" :
    volume = (math.sqrt(2)/12)*a**3
elif polye == "C" :
    volume = a**3
elif polye == "O" :
    volume = (math.sqrt(2)/3)*a**3
elif polye == "D" :
    volume = ((15+(7*math.sqrt(5)))/4)*a**3
elif polye == "I" :
    volume = (((5*(3+math.sqrt(5))))/12)*a**3
else :
    volume = "Polyèdre non connu"

print(volume)
