import numpy as np

with open('day6.txt', 'r') as fichier:
    lignes = fichier.readlines()


lignes = [ligne.strip() for ligne in lignes]
matrice = np.array([list(ligne) for ligne in lignes])
print(matrice)
n, m = matrice.shape
print(n,m)



def chemin(matrice_test):
    count = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    pole = 0
    n, m = matrice_test.shape
    for i in range(n):
        for j in range(m):
            if matrice_test[i,j] == '^':
                x = i
                y = j
    i = 0
    while x>=0 and x<n and y>=0 and y<n:
        
        if i == 30000:
            return 0
        elif matrice_test[x,y] != '#':
            if matrice_test[x,y] != 'X':
                matrice_test[x,y] = 'X'
                count += 1
            x, y = x + directions[pole][0], y + directions[pole][1]
        else:
            x, y = x - directions[pole][0], y - directions[pole][1]
            pole = (pole + 1)%4
            x, y = x + directions[pole][0], y + directions[pole][1]
        i += 1

    return count

def obstacle(matrice):
    count2 = 0
    n,m = matrice.shape
    for i in range(n):
        for j in range(m):
            matrice = np.array([list(ligne) for ligne in lignes])
            if matrice[i,j] == '.':
                matrice[i,j] = '#'
                count = chemin(matrice)
                print(count)
                if count == 0:
                    count2 += 1
                matrice[i,j] = '.'
    return count2
    
obstacle(matrice)



