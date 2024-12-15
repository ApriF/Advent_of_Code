import os
os.chdir("C:\\Users\\cypri\\IdeaProjects\\Advent_of_Code\\day13")

import numpy as np
with open("day13.txt", "r") as file:
    data = file.read()


from fractions import Fraction
result = []
for block in data.strip().split("\n\n"):
    lines = block.split("\n")
    
    # Extraire les coordonnées de Button A
    button_a = lines[0].replace("Button A: X+", "").replace("Y+", "").split(", ")
    button_a = (int(button_a[0]), int(button_a[1]))

    # Extraire les coordonnées de Button B
    button_b = lines[1].replace("Button B: X+", "").replace("Y+", "").split(", ")
    button_b = (int(button_b[0]), int(button_b[1]))

    # Extraire les coordonnées du prix
    prize = lines[2].replace("Prize: X=", "").replace("Y=", "").split(", ")
    prize = (int(prize[0]), int(prize[1]))

    # Ajouter au tableau
    result.append((button_a, button_b, prize))

def solve(result):
    count = 0
    a= 0
    offset = 0
    for machine in result:
        b = np.array([offset + machine[2][0], offset + machine[2][1]])
        A = np.array([[machine[0][0], machine[1][0]], [machine[0][1], machine[1][1]]])
        X = np.linalg.solve(A,b)

        #print(machine, int(X[0]), X[0])
        if abs(round(X[0])- X[0]) < 0.0000000000001 and X[0] > 0 and X[1]> 0:
            if machine[0][0]*round(X[0]) + machine[1][0]*round(X[1]) == b[0] or machine[0][1]*round(X[0]) + machine[1][1]*round(X[1]) == b[1]:
                #print(machine[0][0]*round(X[0]) + machine[1][0]*round(X[1]), b[0], machine[0][1]*round(X[0]) + machine[1][1]*round(X[1]), b[1])
                count += 3*round(X[0]) + round(X[1])
                a += 1
    return count, a

#partie 1
print(solve(result))
def solve_fraction(result):
    count = 0
    a = 0
    offset = 10000000000000

    for machine in result:
        A = [[machine[0][0], machine[1][0]], [machine[0][1], machine[1][1]]]
        b = [offset + machine[2][0], offset + machine[2][1]]


        det = A[0][0] * A[1][1] - A[0][1] * A[1][0]


        x0 = Fraction(A[1][1] * b[0] - A[0][1] * b[1], det)
        x1 = Fraction(A[0][0] * b[1] - A[1][0] * b[0], det)

        if x0.denominator == 1 and x1.denominator == 1 and x0 >= 0 and x1 >= 0:
            cost = 3 * int(x0) + int(x1)
            count += cost
            a += 1

    return count, a
#ârtie 2
solve_fraction(result)