sur = 0


def sure(ligne):

    diff = ligne[1] - ligne[0]
    if abs(diff) >3:
        return False
    for i in range(1, len(ligne) - 1):
        new_diff = ligne[i + 1] - ligne[i]

        if abs(new_diff) > 3 or abs(new_diff) == 0:
            return False
        if diff*new_diff <=0:
            return False
        
        diff = new_diff
    
    return True

def ex2(ligne):
    if sure(ligne):
        return True
    for i in range(len(ligne)):
        if sure(ligne[0:i] + ligne[i+1:len(ligne)]):
            return True
    return False


with open("donnees_day2.txt", "r", encoding="utf-8") as fichier:
    list_of_lists = [list(map(int, line.split())) for line in fichier]
    count = 0
    
    for liste in list_of_lists:
        if ex2(liste):
            count+= 1
    print(count)








