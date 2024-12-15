import numpy as np

with open('day10.txt', 'r') as fichier:
    lignes = fichier.readlines()



chaine = '8901012378121874874309659654987445678903320190120132980110456732'

liste_entiers = [char for char in chaine]
matrice2 = np.array(liste_entiers).reshape(8, 8)

print(matrice2)


lignes = [ligne.strip() for ligne in lignes]
matrice = np.array([list(ligne) for ligne in lignes])
#print(matrice)
n, m = matrice.shape


def cherche(i, j, matrice, vu):
    count = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n,m = matrice.shape
    if matrice[i,j] == '9':
        return 1

        
    for direction in directions:
        new_i, new_j = i + direction[0], j + direction[1]
        if  new_i >=0 and new_i < n and new_j >= 0 and new_j < m and int(matrice[new_i,new_j]) == int(matrice[i,j]) + 1:
            #print(matrice[i,j])
            count += cherche(new_i, new_j, matrice, vu)

    if count==0:
        return 0
            
    return count


def run(part, matrice):
    n, m = matrice.shape
    if part == 1:
        count = 0
        for i in range(n):
            for j in range(m):
                if matrice[i,j] == '0':
                    vu = []
                    count += cherche(i, j, matrice, vu)
                    print(count)
        return count
                    
run(1,matrice)