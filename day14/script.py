import os
os.chdir("C:\\Users\\cypri\\IdeaProjects\\Advent_of_Code\\day14")

import numpy as np
with open("day14.txt", "r") as file:
    data = file.read()

lines = data.strip().split("\n")
result = []

for line in lines:
    parts = line.split()
    # Extraction des tuples p et v
    p = tuple(map(int, parts[0].split('=')[1].split(',')))
    v = tuple(map(int, parts[1].split('=')[1].split(',')))
    # Ajout à la liste sous forme de matrice
    result.append([p, v])




def run(matrice):
    n = len(matrice)
    
    largeur = 101
    hauteur = 103
    temps = 100
    quadrants = [0, 0, 0, 0]
    for i in range(n):
        p = matrice[i][0]
        v = matrice[i][1]
        
        x = (p[0] + temps*v[0])%largeur
        y = (p[1] + temps*v[1])%hauteur
        
        if x < largeur//2:
            if y < hauteur//2:
                quadrants[0] += 1
            elif y> hauteur//2:
                quadrants[1] += 1
        elif x > largeur//2:
            if y < hauteur//2: 
                quadrants[2] += 1
            elif y > hauteur//2: 
                quadrants[3] += 1
    return quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3]

print(run(result))


def recherche(grille, vu, cle):
    count = 0
    if vu[cle] == False:
        count += 1
        vu[cle] = True 
        if (cle[0] + 1, cle[1]) in vu.keys():
            count += recherche(grille, vu, (cle[0] + 1, cle[1]))
        if (cle[0] - 1, cle[1]) in vu.keys():
            count += recherche(grille, vu, (cle[0] - 1, cle[1]))
        if (cle[0], cle[1] + 1) in vu.keys():
            count += recherche(grille, vu, (cle[0], cle[1] + 1))
        if (cle[0], cle[1] - 1) in vu.keys():
            count += recherche(grille, vu, (cle[0], cle[1] - 1))
    return count

def print_grid(grid):
    for row in grid:
        print(''.join(row))
def challenge_2(matrice):
    n = len(matrice)
    largeur = 101
    hauteur = 103
    grille = [['.' for _ in range(largeur)] for _ in range(hauteur)]
    bol = True
    
    dico = {}
    vu = {}
    for i in range(n): 
        p = matrice[i][0]
        v = matrice[i][1]
        x = (p[0] + v[0])%largeur
        y = (p[1] + v[1])%hauteur
        dico[(x,y,v[0],v[1])] = False
        vu[(x,y)] = False
        grille[y][x] = '#'

    i= 0
    while bol:
        i += 1
        count = 0
        for cle in vu.keys():
            temp = recherche(grille, vu, cle)
            if temp > count:
                count = temp
            if count >= 40:
                bol = False
                print_grid(grille)
                break
        
        new_dico = {}
        for cle in dico.keys():
            grille[cle[1]][cle[0]] = ' '
            x = (cle[0] + cle[2])%largeur
            y = (cle[1] + cle[3])%hauteur
            new_dico[(x,y, cle[2], cle[3])] = False
            vu[(x,y)] = False
            grille[y][x] = '●'
        dico = new_dico
    return i
            
    
challenge_2(result)




















    
    
