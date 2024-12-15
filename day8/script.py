import numpy as np
import itertools


with open('day8.txt', 'r') as fichier:
    lignes = fichier.readlines()


lignes = [ligne.strip() for ligne in lignes]
matrice = np.array([list(ligne) for ligne in lignes])
print(matrice)
n, m = matrice.shape
print(n,m)


def dictio(matrice):
    n, m = matrice.shape
    dictio = {}
    for i in range(n):
        for j in range(m):
            if matrice[i,j] != '.':
                if matrice[i,j] not in dictio.keys():
                    dictio[matrice[i,j]] = [(i,j)]
                else:
                    dictio[matrice[i,j]].append((i,j))
    locations = []
    for cle in dictio.keys():
        for pair in itertools.combinations(dictio[cle], r=2):
            locations = compte(pair[0], pair[1], n, m, locations)
    return len(locations)

def compte(pair1, pair2 , n, m, locations):
    co = 0
    diffx = pair1[0] - pair2[0]
    diffy = pair1[1] - pair2[1]
    
    anti1y, anti1x = pair1[0] + diffx, pair1[1] + diffy
    anti2y, anti2x = pair2[0] - diffx, pair2[1] - diffy

    if anti1y>= 0 and anti1y<n and anti1x >=0 and anti1x <m and ((anti1y, anti1x) not in locations):
        co += 1
        locations.append((anti1y, anti1x))
    if anti2y>= 0 and anti2y<n and anti2x >=0 and anti2x <m and ((anti2y, anti2x) not in locations):
        co += 1 
        locations.append((anti2y, anti2x))

    return locations
                
def compte2(pair1, pair2 , n, m, locations):
    diffx = pair1[0] - pair2[0]
    diffy = pair1[1] - pair2[1]

    anti1y, anti1x = pair1[0], pair1[1]
    anti2y, anti2x = pair2[0], pair2[1]

    while anti1y>= 0 and anti1y<n and anti1x >=0 and anti1x <m:
        if (anti1y, anti1x) not in locations: 
            locations.append((anti1y, anti1x))
        anti1y, anti1x = anti1y + diffx, anti1x + diffy

    while anti2y>= 0 and anti2y<n and anti2x >=0 and anti2x <m:
        if (anti2y, anti2x) not in locations:
            locations.append((anti2y, anti2x))
        anti2y, anti2x = anti2y - diffx, anti2x - diffy

    return locations

def dictio2(matrice):
    n, m = matrice.shape
    dictio = {}
    for i in range(n):
        for j in range(m):
            if matrice[i,j] != '.':
                if matrice[i,j] not in dictio.keys():
                    dictio[matrice[i,j]] = [(i,j)]
                else:
                    
                    dictio[matrice[i,j]].append((i,j))
    locations = []
    for cle in dictio.keys():
        for pair in itertools.combinations(dictio[cle], r=2):
            locations = compte2(pair[0], pair[1], n, m, locations)
    return len(locations)

dictio(matrice)
dictio2(matrice)