# Écrire un programme qui imprime la valeur du volume d’une sphère de rayon r, float lu en entrée.

# On rappelle que le volume d’une sphère de rayon r est donné par la formule : \frac{4}{3}\pi{r^3}

# Exemple 1
# Avec la donnée lue suivante :

# 1.0
# le résultat à imprimer vaudra (approximativement) :

# 4.1887902047863905
# Exemple 2
# Avec la donnée lue suivante :

# 0.5
# le résultat à imprimer vaudra (approximativement) :

# 0.5235987755982988


Réponse 

import math

r = float(input())

print(float(4/3)*(math.pi)*(r**3))
