

with open('day7.txt', 'r') as fichier:
    lignes = fichier.readlines()

resultat = []
for ligne in lignes:
    identifiant, valeurs = ligne.split(':')
    valeurs_liste = list(map(int, valeurs.split()))
    resultat.append([int(identifiant)] + valeurs_liste)


def test(liste, operators):
    result = liste[0]
    value = liste[1]
    for i in range(len(operators)):
        if operators[i] == '+':
            value = value + liste[i+2]
        
        if operators[i] == '*':
            value = value*liste[i+2]
    
    if result == value:
        return True
    
def all_tests_part1(liste):
    oper = []
    long = len(liste) - 2
    
    for i in range(2**long):
        oper.append(operators_part1(i, 2**long))
    
    for i in range(len(oper)):
        if test(liste, oper[i]):
            return True
    return False
    
def operators_part1(indice, n):
    if n==2:
        if indice == 0:
            return '+'
        if indice ==1:
            return '*'
    if indice < n//2:
        return '+' + operators_part1(indice, n//2)
    else:
        return '*' + operators_part1(indice-n//2, n//2)
    
def main_part1(resultat):
    count = 0
    for i in range(len(resultat)):
        if all_tests_part1(resultat[i]):
            count += resultat[i][0]
    return count



def test_part2(liste, operators):
    result = liste[0]
    value = liste[1]
    for i in range(len(operators)):
        if operators[i] == '+':
            value = value + liste[i+2]
        
        if operators[i] == '*':
            value = value*liste[i+2]
    
        if operators[i] == '|':
            value = int(f"{value}" + f"{liste[i+2]}")
    if result == value:
        return True  


def all_tests_part2(liste):
    oper = []
    long = len(liste) - 2
    
    for i in range(3**long):
        oper.append(operators_part2(i, 3**long))
    
    for i in range(len(oper)):
        if test_part2(liste, oper[i]):
            return True
    return False


def operators_part2(indice, n):
    if n==3:
        if indice == 0:
            return '+'
        if indice ==1:
            return '*'
        if indice ==2:
            return '|'
        
    if indice < n//3:
        return '+' + operators_part2(indice, n//3)
    elif indice< 2* (n//3):
        return '*' + operators_part2(indice-n//3, n//3)
    else:
        return '|' + operators_part2(indice-2*(n//3), n//3)



def main_part2(resultat):
    count = 0
    for i in range(len(resultat)):
        print(i)
        if all_tests_part2(resultat[i]):
            count += resultat[i][0]
    return count


main_part2(resultat)




