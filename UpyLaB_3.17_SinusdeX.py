
On peut calculer approximativement le sinus d’un nombre x en effectuant la sommation des premiers termes de la série (une série est une somme infinie) :

sin(x) =  x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + ...

où x est exprimé en radians et 3! désigne la factorielle de 3.

Écrire un programme qui lit une valeur flottante x en entrée et imprime une approximation de sin(x)
Cette approximation sera obtenue en additionnant successivement les différents termes de la série jusqu’à ce que la valeur du terme devienne inférieure (en valeur absolue) à une constante \epsilon que l’on fixera à 10^{-6}.






x = float(input())
def sin2(x):
    xc = x * x  
    n, t = 0, x
    s1 = t
    while True:
        n += 1
        t *= -xc / (2 * n * (2 * n + 1))
        s2 = s1 + t
        if s2 == s1:
            break
        s1 = s2
    return s2


print(sin2(x))
