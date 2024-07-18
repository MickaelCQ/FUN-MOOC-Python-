Dans cet exercice, nous revenons sur le petit jeu de devinette.

Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret) compris entre 0 et 100, bornes incluses. Ensuite, le joueur doit deviner ce nombre en utilisant le moins d’essais possible.

À chaque tour, le joueur est invité à proposer un nombre et le programme doit donner une réponse parmi les suivantes :

« Trop grand » : si le nombre secret est plus petit que la proposition et qu’on n’est pas au maximum d’essais

« Trop petit » : si le nombre secret est plus grand que la proposition et qu’on n’est pas au maximum d’essais

« Gagné en n essai(s) ! » : si le nombre secret est trouvé

« Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret.

Exemple 1
Une partie gagnée (après la génération du nombre à deviner) :

NB : Les nombres sont les valeurs saisies par l’utilisateur, et les textes sont imprimés par le programme.

50
Trop grand
8
Trop petit
20
Trop petit
27
Gagné en 4 essai(s) !
Exemple 2
Une partie perdue (après la génération du nombre à deviner) :

50
Trop grand
24
Trop petit
37
Trop petit
43
Trop grand
40
Trop petit
41
Perdu ! Le secret était 42
Consignes
Attention, au dernier essai, le programme ne doit afficher ni « Trop petit » ni « Trop grand », mais le verdict comme illustré plus haut.

Pour qu’Upylab puisse tester que votre solution est correcte, il faut que vous respectiez strictement la séquence décrite dans l’énoncé. Si par exemple, vous n’affichez pas « Trop petit » ou « Trop grand », le nombre suivant ne sera pas fourni par le système et votre solution sera considérée comme incorrecte.

En pratique, pour la génération du nombre secret, vous devez débuter votre code comme suit :

import random
NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)


import random
random1 = random.randint(0,100)

max_essai = 6
n= 0
reponse = 0
while max_essai > n and reponse != random1 :
    n = n + 1
    reponse = int(input())

    if n == 6 and reponse != random1:
        print("Perdu ! Le secret était ", random1)

    elif random1 == reponse :
        print("Gagné en ", n, "essai(s) !")
        random1 == reponse

    elif reponse > random1 and 6 > n :
        print("Trop grand")

    elif random1 > reponse and 6 > n :
        print("Trop petit")



