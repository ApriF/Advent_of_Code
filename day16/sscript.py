import numpy as np
import os
os.chdir("C:\\Users\\cypri\\IdeaProjects\\Advent_of_Code\\day16")
with open('test.txt', 'r') as fichier:
    lignes = fichier.readlines()


lignes = [ligne.strip() for ligne in lignes]
matrice = np.array([list(ligne) for ligne in lignes])

def print_grid(grid):
    for row in grid:
        print(''.join(row))



n, m = len(matrice), len(matrice[0])
directions = [(0, 1),(-1, 0),(0, -1),(1, 0)]

def cherche(stack, visite, count, direction):

    if len(stack) == 0:

        return visite
    else:
        y, x = stack.pop()
        if (x,y) not in visite.keys():
            visite[(x,y)] = count
            
            if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                stack.append((y+directions[direction][0], x+directions[direction][1]))
                cherche(stack, visite, count + 1, direction)
            
            direction = (direction + 1)%4
            if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                stack.append((y+directions[direction][0], x+directions[direction][1]))
                cherche(stack, visite, count + 1 + 1000, direction)
            
            direction = (direction + 1)%4
            # if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
            #     stack.append((y+directions[direction][0], x+directions[direction][1]))
            #     cherche(stack, visite, count + 1 + 2000, direction)
            
            direction = (direction + 1)%4
            if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                stack.append((y+directions[direction][0], x+directions[direction][1]))
                cherche(stack, visite, count + 1 + 1000, direction)

        else: 
            if count < visite[(x,y)]:
                visite[(x,y)] = count
                if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                    stack.append((y+directions[direction][0], x+directions[direction][1]))
                    cherche(stack, visite, count + 1, direction)
                
                direction = (direction + 1)%4
                if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                    stack.append((y+directions[direction][0], x+directions[direction][1]))
                    cherche(stack, visite, count + 1 + 1000, direction)
                
                direction = (direction + 1)%4
                # if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                #     stack.append((y+directions[direction][0], x+directions[direction][1]))
                #     cherche(stack, visite, count + 1 + 2000, direction)
                
                direction = (direction + 1)%4
                if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                    stack.append((y+directions[direction][0], x+directions[direction][1]))
                    cherche(stack, visite, count + 1 + 1000, direction)
            cherche(stack, visite, count, direction)


def solve():
    visite = {}
    stack = []
    for i in range(n):
        for j in range(m):
            if matrice[i][j] == 'S':
                x, y = j, i
            if matrice[i][j] == 'E':
                endx, endy = j,i
                matrice[i][j] = '.'
                
    stack.append((y,x))
    count = 0
    direction = 0
    cherche(stack, visite, count, direction)
    print(visite)
    return visite[(endx, endy)]

#print(solve())

def cherche2(stack, visite, count, direction, pred):

    if len(stack) == 0:
        return visite
    else:
        y, x = stack.pop()
        if (x,y) not in visite.keys():
            visite[(x,y)] = count
            pred[(y,x)] = [(y - directions[direction][0], x-directions[direction][1])]
            if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                stack.append((y+directions[direction][0], x+directions[direction][1]))
                cherche2(stack, visite, count + 1, direction, pred)
            
            direction = (direction + 1)%4
            if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                stack.append((y+directions[direction][0], x+directions[direction][1]))
                cherche2(stack, visite, count + 1 + 1000, direction, pred)
                
            direction = (direction + 1)%4
            direction = (direction + 1)%4
            if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                stack.append((y+directions[direction][0], x+directions[direction][1]))
                cherche2(stack, visite, count + 1 + 1000, direction, pred)
        else: 
            if (x,y) == (9,7):
                print(count, visite[x,y])
            if count < visite[(x,y)]:
                visite[(x,y)] = count
                pred[(y,x)] = [(y - directions[direction][0], x-directions[direction][1])]
                if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                    stack.append((y+directions[direction][0], x+directions[direction][1]))
                    cherche2(stack, visite, count + 1, direction, pred)
                
                direction = (direction + 1)%4
                if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                    stack.append((y+directions[direction][0], x+directions[direction][1]))
                    cherche2(stack, visite, count + 1 + 1000, direction, pred)
                
                direction = (direction + 1)%4
                direction = (direction + 1)%4
                if matrice[y+directions[direction][0]][x+directions[direction][1]] == '.':
                    stack.append((y+directions[direction][0], x+directions[direction][1]))
                    cherche2(stack, visite, count + 1 + 1000, direction, pred)
                    
            elif count == visite[(x,y)]:
                if (y - directions[direction][0], x-directions[direction][1]) not in pred[(y,x)] and matrice[(y - directions[direction][0], x-directions[direction][1])] == '.':
                    pred[(y,x)].append((y - directions[direction][0], x-directions[direction][1]))
            cherche2(stack, visite, count, direction, pred)


def retrouver_chemins(pred, y, x, starty, startx, liste, visites=None):
    if visites is None:
        visites = set()

    if (y, x) == (starty, startx):
        return

    if (y, x) not in visites:
        visites.add((y, x))  # Marquer comme visité
        for predecessor in pred.get((y, x), []):
            if predecessor == (6,9) or predecessor == (1,12):
                print((y,x))
            if predecessor not in liste:
                liste.append(predecessor)
            # Explore chaque prédécesseur séparément
            retrouver_chemins(pred, predecessor[0], predecessor[1], starty, startx, liste, visites)


    

def solve2():
    visite = {}
    stack = []
    pred = {}
    for i in range(n):
        for j in range(m):
            if matrice[i][j] == 'S':
                startx, starty = j, i
            if matrice[i][j] == 'E':
                endx, endy = j,i
                matrice[i][j] = '.'
    print_grid(matrice)
    stack.append((starty, startx))
    count = 0
    direction = 0
    cherche2(stack, visite, count, direction, pred)
    print(pred)

    liste = []
    visités = set()
    retrouver_chemins(pred, endy, endx, starty, startx, liste, visités)

    print("\nListe des sommets sur les chemins optimaux :")
    print(liste)
    return len(liste)

solve2()