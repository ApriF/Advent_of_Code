
import numpy as np

with open('day4.txt', 'r') as fichier:
    lignes = fichier.readlines()


lignes = [ligne.strip() for ligne in lignes]
matrice = np.array([list(ligne) for ligne in lignes])

def check_direction(grid, x, y, direction):
    word = "XMAS"
    word_len = len(word)
    dx, dy = direction
    
    # Vérification si le mot dépasse les limites de la grille
    for i in range(word_len):
        nx, ny = x + i * dx, y + i * dy
        print(nx,ny)
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
            return False
    return True


def search_xmas(grid):
    # Directions : (dx, dy) -> droit, bas, gauche, haut, diagonale (bas-gauche), diagonale (bas-droite), diagonale (haut-gauche), diagonale (haut-droite)
    directions = [
        (0, 1),   # Horizontal droit
        (0, -1),  # Horizontal gauche
        (1, 0),   # Vertical bas
        (-1, 0),  # Vertical haut
        (1, -1),  # Diagonale bas-gauche
        (1, 1),   # Diagonale bas-droite
        (-1, -1), # Diagonale haut-gauche
        (-1, 1)   # Diagonale haut-droite
    ]
    
    count = 0
    # Parcours de la grille
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Vérifier chaque direction
            for direction in directions:
                if check_direction(grid, i, j, direction):
                    count += 1
    return count


count = search_xmas(matrice)

print(f"Le mot 'XMAS' apparaît {count} fois.")
