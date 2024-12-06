
import numpy as np

with open('day4.txt', 'r') as fichier:
    lignes = fichier.readlines()


lignes = [ligne.strip() for ligne in lignes]
matrice = np.array([list(ligne) for ligne in lignes])

def check_direction(grid, x, y, direction):
    word = "MAS"
    word_len = len(word)
    dx, dy = direction

    

    for i in range(word_len):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx, ny] != word[i]:
            return False
        
    return True


def check_cotes(grid, x, y):
    if check_direction(grid, x-1, y-1, (1, 1)) or check_direction(grid, x+1, y+1, (-1, -1)):
        if check_direction(grid, x+1, y-1, (-1, 1)) or check_direction(grid, x-1, y+1, (1, -1)):
            print('vrai')
            return True

def search_xmas(grid):
    # Directions 
    directions = [
        [(1,1), (1, -1)], [(-1, -1), (1, -1)], [(1,1), (-1, 1)], [(-1, -1), (-1,1)]]
    count = 0
    # Parcours de la grille
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i,j] == 'A':
                if check_cotes(grid, i,j):
                    count += 1
    return count


count = search_xmas(matrice)

print(count)
