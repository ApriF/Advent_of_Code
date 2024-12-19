import os
os.chdir("C:\\Users\\cypri\\IdeaProjects\\Advent_of_Code\\day19")
with open('day19.txt', 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]
if lines:
    patterns = lines[0].split(', ')
    liste = [line for line in lines[2:]]

#print(patterns)

def faisable(string, vu):
    if string in vu.keys():
        if vu[string]:
            return True
        else:
            return False
    else:
        for j in range(len(patterns)):
            if string == patterns[j]:
                vu[string] = True
                return True
            length = len(patterns[j])
            if length <= len(string) and string[:length] == patterns[j]:
                if faisable(string[length:], vu):
                    return True
        return False

def run():
    count = 0
    vu = {}
    for i in range(len(liste)):
        string = liste[i]
        if faisable(string, vu):
            count += 1
    return count

print(run())

def faisable_count(string, vu_count, vu_count_2, count, decoupe, mots):
    if string not in vu_count.keys():
        vu_count[string] = []
    #print(vu_count_2, string, mots)
    if string in vu_count_2.keys():
        for i in range(len(mots)):
            if mots[i] not in vu_count_2.keys():
                vu_count_2[mots[i]] = vu_count_2[string]
            else:
                vu_count_2[mots[i]] += vu_count_2[string]
        count += vu_count_2[string]
    else:
        for j in range(len(patterns)):
            #print(string, patterns[j])
            length = len(patterns[j])
            if string == patterns[j]:
                decoupe.append(patterns[j])
                mots.append(string)
                for i in range(len(mots)):
                    if decoupe[i:] not in vu_count[mots[i]]:
                        vu_count[mots[i]].append(decoupe[i:])
                    if mots[i] not in vu_count_2.keys():
                        vu_count_2[mots[i]] = 1 
                    else:
                        vu_count_2[mots[i]] += 1   
                count += 1
                decoupe.pop()
                mots.pop()
                
            if length <= len(string) and string[:length] == patterns[j]:
                decoupe.append(patterns[j])
                mots.append(string)
                count = faisable_count(string[length:], vu_count, vu_count_2, count, decoupe, mots)
                decoupe.pop()
                mots.pop()
    return count

def run_2():
    count = 0
    vu = {}
    vu_count = {} 
    vu_count_2 = {}
    for i in range(len(liste)):
        string = liste[i]
        if faisable(string, vu):
            ways = 0
            decoupe = []
            mots = []
            ways = faisable_count(string, vu_count, vu_count_2, ways, decoupe, mots)

            count += ways
    return count

run_2()

