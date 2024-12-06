with open('day5.txt', 'r', encoding="utf-8") as fichier:
    lignes = fichier.readlines()
    liste = []
    i = 0
    for _ in range(len(lignes)):
        try:
            a, b = map(int, lignes[i].split('|'))
            liste.append((a, b))
            i += 1
        except Exception as e:
            i+= 1
            break
    
    patterns = []
    for _ in range(len(lignes)-i):
        ligne = lignes[i].strip()
        patterns.append(list(map(int, ligne.split(','))))
        i += 1

def get_indice(number,liste):
    for i in range(len(liste)):
        if number == liste[i]:
            return i

def identify(pattern, liste):
    if len(pattern) == 1:
        return True
    else:
        for i in range(len(liste)):
            if pattern[0] == liste[i][1] and (liste[i][0] in pattern):
                print(liste[i], pattern)
                return False
        return identify(pattern[1:], liste)

def correct(pattern,liste):
    if identify(pattern, liste) == False:
        for _ in range(len(pattern)):
            for i in range(len(pattern)):
                for j in range(len(liste)):
                    if pattern[i] == liste[j][1] and (liste[j][0] in pattern):
                        print(liste[j], pattern)
                        indice = get_indice(liste[j][0], pattern)
                        if indice > i:
                            pattern[indice] = pattern[i]
                            pattern[i] = liste[j][0]
        return correct(pattern,liste)
                
    else:
        return pattern

def run(pattern, liste):
    count = 0
    count2 = 0
    for i in range(len(pattern)):
        if identify(pattern[i], liste):
            indice = len(pattern[i])//2
            count += pattern[i][indice]
        else:
            pattern[i] = correct(pattern[i], liste)
            indice = len(pattern[i])//2
            count2 += pattern[i][indice]
            
    return count, count2

run(patterns, liste)