Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat.
La première donnée lue ne fait pas partie des valeurs à sommer. Elle détermine si la liste contient un nombre déterminé à l’avance de valeurs à lire ou non :

si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs à lire et à sommer ;

si elle est égale à -1, cela signifie qu’elle est suivie d’une liste de données à lire qui sera terminée par le caractère "F" signifiant que la liste est terminée.




Réponse

Ninitial = int(input())
Result = 0
Nsomme2 = 0
i = 0

if Ninitial >= 0 :
    for i in range(Ninitial):
        Nsomme = int(input())
        Result += Nsomme
    print(Result)
elif Ninitial == -1:
    int(Nsomme2)
    while Nsomme2 != "F":
            Nsomme2 = input()
            if Nsomme2 != "F":
                Result += int(Nsomme2)
    print(Result)
