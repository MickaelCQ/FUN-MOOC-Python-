Dans mon casino, ma roulette comporte 13 numéros de 0 à 12 comme montrés ci-dessous :

https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/roulette.jpg
Roulette

Le joueur a plusieurs types de paris possibles :

il peut choisir de parier sur le numéro sortant, et dans ce cas, s’il gagne, il remporte douze fois sa mise ;

il peut choisir de parier sur la parité du numéro sortant (pair ou impair), et dans ce cas, s’il gagne, il remporte deux fois sa mise ;

enfin, il peut choisir de parier sur la couleur du numéro sortant (rouge ou noir), et dans ce cas aussi, s’il gagne, il remporte deux fois sa mise.

Si le joueur perd son pari, il ne récupère pas sa mise.

Pour simplifier, on suppose que le numéro 0 n’est ni rouge ni noir, mais est pair. Pour simplifier encore, on suppose que le joueur mise systématiquement 10 euros.

Écrire un programme qui aide le croupier à déterminer la somme que le casino doit donner au joueur.

Le programme lira, dans l’ordre, deux nombres entiers en entrée : le pari du joueur (représenté par un nombre entre 0 et 16, voir description plus bas), et le numéro issu du tirage (nombre entre 0 et 12). Le programme affichera alors le montant gagné par le joueur.

Entrées pour le pari du joueur :

nombre entre 0 et 12 : le joueur parie sur le numéro correspondant

13 : le joueur parie sur pair

14 : le joueur parie sur impair

15 : le joueur parie sur la couleur rouge

16 : le joueur parie sur la couleur noire.


Réponse :

pari = int(input())
tirage =  int(input())

pairList = [0,2,4,6,8,10,12]
impairList = [1,3,5,7,9,11]

BlackList = [2,4,6,8,10,11]
RedList = [1,3,5,7,9,12]

if 0 <= pari <= 12 :
    if pari == tirage:
        gain = 120
    else:
        gain = 0

if pari == 13 :
    if tirage in pairList:
        gain = 20
    else:
        gain =0

if pari == 14 :
    if tirage in impairList:
        gain = 20
    else:
        gain =0

if pari == 15 :
    if tirage in RedList:
        gain = 20
    else:
        gain = 0
if pari == 16 :
    if tirage in BlackList:
        gain = 20
    else :
        gain = 0

print(gain)
