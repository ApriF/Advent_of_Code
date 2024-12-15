import os
os.chdir("C:\\Users\\cypri\\IdeaProjects\\Advent_of_Code\\day12")



import numpy as np
dico = {}
dico_area = {}
with open('day12.txt', 'r') as fichier:
    lignes = fichier.readlines()


lignes = [ligne.strip() for ligne in lignes]
matrice = np.array([list(ligne) for ligne in lignes])
print(matrice)
n, m = matrice.shape
def egal(i, j, letter):
        return 0 <= i < n and 0 <= j < m and matrice[i, j] == letter

def calcul_perimeter(matrice, i, j, letter):
    perimeter = 0

    if (i,j) not in dico.keys():
        dico[(i,j)] = True
        for dr, dh in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_i, new_j = i + dr, j + dh
            if not egal(new_i,new_j, letter):
                perimeter += 1
            else:
                perimeter += calcul_perimeter(matrice, new_i, new_j, letter)

    return perimeter

def run(matrice):
    n, m = matrice.shape
    count = 0
    for i in range(n):
        print(i)
        for j in range(m):
            letter = matrice[i,j]

            if (i,j) not in dico.keys():
                letter = matrice[i,j]
                temp = len(dico)
                
                perimeter= calcul_perimeter(matrice, i, j, letter)
                area = len(dico) - temp
                count += area*perimeter

    return count

print(run(matrice))


def calcul_sides(matrice, i, j, letter):
    sides = 0
    new_i, new_j = i+1, j
    while (new_i, new_j) != (i,j):
        while egal(new_i, new_j, letter):
            a=2
            
            
            
def run2(matrice):
    n, m = matrice.shape
    count = 0
    for i in range(n):

        for j in range(m):
            letter = matrice[i,j]

            if (i,j) not in dico.keys():
                letter = matrice[i,j]
                temp = len(dico)
                
                sides = calcul_sides(matrice, i, j, letter)
                area = len(dico) - temp
                count += area*sides

    return count