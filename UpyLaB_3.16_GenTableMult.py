Écrivez un code qui lit un nombre entier strictement positif n et affiche sur n lignes une table de multiplication de taille  n x n, avec, pour i entre 1 et n,  les n premières valeurs multiples de i strictement positives sur la ième ligne.
Ainsi, les n premiers multiples de 1 strictement positifs (0 non compris) sont affichés sur la première ligne, les n premiers multiples de 2 sur la deuxième, et cætera.



  réponse
  
n = int(input())+1
i = 0
j = 0


for i in range(1, n):
    for j in range(1,n):
        multiple = i * j
        print(multiple,sep=" ", end= " ")
    print()
