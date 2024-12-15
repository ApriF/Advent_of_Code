import os
os.chdir("C:\\Users\\cypri\\IdeaProjects\\Advent_of_Code\\day15")

import numpy as np
grille = []
sequence = ""

# Lecture et séparation des données d'un fichier
with open("day15.txt", "r") as fichier:
    contenu = fichier.read()

# Séparation des données grâce à deux retours à la ligne
parties = contenu.split("\n\n")
raw_grid = parties[0].splitlines()
sequence = parties[1].replace("\n", "")

grille = [list(ligne) for ligne in raw_grid]
n,m = len(grille) , len(grille[0])



def print_grid(grid):
    for row in grid:
        print(''.join(row))

def deplacer(x, y, direction):
    new_y, new_x = y + direction[0], x + direction[1]

    if grille[new_y][new_x] == '.':
        grille[new_y][new_x] = '@'
        grille[y][x] = '.'
        return new_y, new_x
    
    if grille[new_y][new_x] == '#':
        return y, x
    
    if grille[new_y][new_x] == 'O':
        i, j = new_y, new_x
        while grille[i][j] == 'O':
            i, j = i + direction[0], j + direction[1]
        if grille[i][j] == '#':
            return y, x
        if grille[i][j] == '.':
            grille[i][j] = 'O'
            grille[new_y][new_x] = '@'
            grille[y][x] = '.'
            return new_y, new_x
    
def solve():
    
    
    for i in range(n):
        for j in range(m):
            if grille[i][j] == '@':
                y, x = i, j

    
    
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    for i in range(len(sequence)):
        if sequence[i] == '<':
            y, x = deplace(x, y, directions[1])
        if sequence[i] == '>':
            y, x = deplace(x, y, directions[0])        
        if sequence[i] == 'v':
            y, x = deplace(x, y, directions[2]) 
        if sequence[i] == '^':
            y, x = deplace(x, y, directions[3])
    
    count = 0
    for i in range(n):
        for j in range(m):
            if grille[i][j] == 'O':
                count += 100*i + j
    return count

#print(solve())

grille_2 = [['.' for _ in range(2*m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grille[i][j] == '.':
            grille_2[i][2*j] = '.'
            grille_2[i][2*j + 1] = '.'
        if grille[i][j] == '#':
            grille_2[i][2*j] = '#'
            grille_2[i][2*j + 1] = '#'
        if grille[i][j] == 'O':
            grille_2[i][2*j] = '['
            grille_2[i][2*j + 1] = ']'
        if grille[i][j] == '@':
            grille_2[i][2*j] = '@'
            grille_2[i][2*j + 1] = '.'


def condition(direction, stack):
    if len(stack) == 0:
        return True
    else:
        x, y = stack.pop()
        new_y = y + direction[0] 
        if grille_2[new_y][x] == '#':
            return False
        if grille_2[new_y][x] == ']' and grille_2[y][x] == '[':
            stack.append((x-1,new_y))
            stack.append((x,new_y))
        if grille_2[new_y][x] == ']' and grille_2[y][x] == ']':
            stack.append((x-1,new_y))
            stack.append((x,new_y))
        if grille_2[new_y][x] == '[' and grille_2[y][x] == ']':
            stack.append((x,new_y))
            stack.append((x+1,new_y))
        return condition(direction, stack) 


def deplacer_2(x1, x2,y,direction):
    new_y = y + direction[0]

    if grille_2[new_y][x1] == ']':
        deplacer_2(x1-1, x1, new_y, direction)
    if grille_2[new_y][x1] == '[':
        deplacer_2(x1, x2, new_y, direction)
    if grille_2[new_y][x2] == '[':
        deplacer_2(x2, x2 + 1, new_y, direction)
    if grille_2[new_y][x1] == '.' and grille_2[new_y][x2] == '.':
        grille_2[new_y][x1] = '['
        grille_2[new_y][x2] = ']'
        grille_2[y][x1] = '.'
        grille_2[y][x2] = '.'
    grille_2[new_y][x1] = '['
    grille_2[new_y][x2] = ']'


        

def deplace(x, y, direction, bol):
    new_y, new_x = y + direction[0], x + direction[1]
    if grille_2[new_y][new_x] == '.':
        grille_2[new_y][new_x] = '@'
        grille_2[y][x] = '.'
        return new_y, new_x
    
    if grille_2[new_y][new_x] == '#':
        return y, x
    
    if grille_2[new_y][new_x] == ']':
        i, j = new_y, new_x
        passage = []
        passage.append((i,j))
        if bol:
            stack = []
            stack.append((x-1,new_y))
            stack.append((x,new_y))
            if condition(direction, stack):
                deplacer_2(x-1,x,new_y,direction)
                grille_2[new_y][new_x] = '@'
                grille_2[new_y][new_x - 1] = '.'
                grille_2[y][x] = '.'
                return new_y, new_x
            return y, x
        else:
            while grille_2[i][j] == '[' or grille_2[i][j] == ']':
                i, j = i + direction[0], j + direction[1]
                passage.append((i,j))
            if grille_2[i][j] == '#':
                return y, x
            else:
                count = 0
                for u in range(len(passage)):
                    if count%2 == 0:
                        grille_2[passage[u][0]][passage[u][1]] = '['
                    if count%2 == 1:
                        grille_2[passage[u][0]][passage[u][1]] = ']'
                    count += 1
                grille_2[y][x] = '.'
                grille_2[new_y][new_x] = '@'
                return new_y, new_x
    
    if grille_2[new_y][new_x] == '[':
        i, j = new_y, new_x
        passage = []

        if bol:
            stack = []
            stack.append((x,new_y))
            stack.append((x+1,new_y))
            if condition(direction, stack):
                deplacer_2(x,x+1,new_y,direction)
                grille_2[new_y][new_x] = '@'
                grille_2[new_y][new_x + 1] = '.'
                grille_2[y][x] = '.'
                return new_y, new_x
            return y, x
        else:
            while grille_2[i][j] == '[' or grille_2[i][j] == ']':
                i, j = i + direction[0], j + direction[1]
                passage.append((i,j))
            if grille_2[i][j] == '#':
                return y, x
            else:
                count = 0
                for u in range(len(passage)):
                    if count%2 == 0:
                        grille_2[passage[u][0]][passage[u][1]] = '['
                    if count%2 == 1:
                        grille_2[passage[u][0]][passage[u][1]] = ']'
                    count += 1
                grille_2[y][x] = '.'
                grille_2[new_y][new_x] = '@'
                return new_y, new_x

                        

def solve_part_2():
    n = len(grille_2)
    m = len(grille_2[0])
    for i in range(n):
        for j in range(m):
            if grille_2[i][j] == '@':
                y, x = i, j

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    
    for i in range(len(sequence)):
        if sequence[i] == '<':
            y, x = deplace(x, y, directions[1], False)
        if sequence[i] == '>':
            y, x = deplace(x, y, directions[0], False)
        if sequence[i] == 'v':
            y, x = deplace(x, y, directions[2], True) 
        if sequence[i] == '^':
            y, x = deplace(x, y, directions[3], True)


    count = 0
    for i in range(n):
        for j in range(m):
            if grille_2[i][j] == '[':

                count += 100*i + j
    return count


solve_part_2()









