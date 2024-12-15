
with open('day9.txt', 'r') as fichier:
    ligne = fichier.readlines()[0]


mat = []
for i in range(len(ligne)):
    mat.append(ligne[i])

def run(part, ligne, string):
    #j'ai len(ligne) = 19999
    reverse = ligne[::-1]
    if part == 1:
        
        count = 0
        long = calcul_longueur(ligne)
        it = 0
        i_reverse, used = 0, 0
        n = len(ligne)
        for i in range(n):
            somme = 0
            if i%2 == 0:
                it, somme, bol = calcul_somme(long, it, ligne, i)
                count += somme
                if bol:
                    return count
            
            else:
                for _ in range(int(ligne[i])):
                    if it == long:
                        return count
                    if used < int(reverse[i_reverse]):
                        count += it*((n-i_reverse)//2)
                        it += 1
                        used += 1
                    else:
                        used = 0
                        i_reverse += 2
                        assert int(reverse[i_reverse]) !=0
                        count += it*((n-i_reverse)//2)
                        it += 1
                        used += 1
    
    if part == 2:
        count = 0
        liste = []
        
        n = len(ligne)
        for i in range(n):
            if i%2 == 0:
                if ligne[i] != '.':
                    for _ in range (int(ligne[i])):
                        liste.append(i//2)
                        ligne[i] = '.'
                else:
                    for _ in range(int(string[i])):
                        liste.append(0)
            else:
                if ligne[i] != '.':
                    trou = int(ligne[i])
                    for j in range(0,n,2):
                        if ligne[n-1-j] != '.' and int(ligne[n-j-1]) <= trou:
                            for _ in range (int(ligne[n-1-j])):
                                liste.append((n-1-j)//2)
                            trou = trou - int(ligne[n-1-j])
                            ligne[n-1-j] = '.'
                        if trou == 0:
                            break
                    for _ in range(trou):
                        liste.append(0)
                    

        for i in range(len(liste)):
            count += i*liste[i]
        
        return count
                    
                
            
        

def calcul_longueur(ligne):
    c = 0
    for i in range(len(ligne)):
        if i%2 == 0:
            c += int(ligne[i])
    return c

def calcul_somme(long, it, ligne, i):
    somme = 0
    bol = False
    for j in range(int(ligne[i])):
        if it == long:
            bol = True
            break
        somme += it*(i//2)
        print(i//2)
        it += 1
    return it, somme, bol


#run(1, ligne)
run(2, mat, ligne)
