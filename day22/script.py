import os
os.chdir("C:\\Users\\cypri\\IdeaProjects\\Advent_of_Code\\day22")

with open("test.txt") as fichier:
    data = fichier.readlines()

liste = [int(ligne.strip()) for ligne in data]

print(liste)

def new_secret_number(number):
    number = ((number*64)^number)%16777216
    number = ((number//32)^number)%16777216
    number = ((number*2048)^number)%16777216
    return number

def run():
    count = 0
    for i in range(len(liste)):
        secret = []
        number = liste[i]
        while len(secret) < 2000:
            number = new_secret_number(number)
            secret.append(number)
        count += secret[1999]
        print(count)
    return count

run()

def run_2():
    length = len(liste)
    secret_numbers = [[0 for _ in range(2000)] for _ in range(length)]
    counts = {}
    for i in range(length):
        n = liste[i]
        for j in range(2000):
            secret_numbers[i][j] = n
            if j >=4:
                suite = (secret_numbers[i][j] - secret_numbers[i][j-1], 
                secret_numbers[i][j-1] - secret_numbers[i][j-2],
                secret_numbers[i][j-2] - secret_numbers[i][j-3],
                secret_numbers[i][j-3] - secret_numbers[i][j-4])
                print(suite, counts)
                if suite in counts.keys():
                    counts[suite] += n%10
                else:
                    counts[suite] = n%10
            n = new_secret_number(n)
    
    maxi = 0
    for key in counts.keys():
        if counts[key] > maxi:
            maxi = counts[key]
    return maxi


run_2()















