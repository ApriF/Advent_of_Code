

gauche = []
droite = []


def tri (liste, element):
    liste.append(element)
    n = len(liste)
    for i in range(n-1):
        if liste[n-i-1] < liste[n-i-2]:
            liste[n-i-1] = liste[n-i-2]
            liste[n-i-2] = element

with open("donnes_day1.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        tri(gauche, int(ligne.strip()[0:5]))
        tri(droite, int(ligne.strip()[8:14]))

##Exo 1
compte = 0    
for i in range(len(gauche)):
    compte += abs(droite[i] - gauche[i])
#print(compte)

##Exo 2
count2 = 0
for i in range(len(gauche)):
    if gauche[i] in droite:
        it = 0
        for j in range(len(droite)):
            if droite[j] == gauche[i]:
                it += 1
        count2 += gauche[i]*it
print(count2)