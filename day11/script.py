with open('day11.txt', 'r') as fichier:
    lignes = fichier.readlines()

tableau = lignes[0].split()  # Divise la chaîne par les espaces
print(tableau)


def run(ligne, blinks):
    
    for j in range(blinks):
        new_ligne = []
        print(j)
        for i in range(len(ligne)):
            if ligne[i] == '0':
                new_ligne.append('1')
            
            elif len(ligne[i])%2 == 0:
                new_ligne.append(ligne[i][:len(ligne[i])//2])
                new_ligne.append(arrange_zeros(ligne[i][len(ligne[i])//2:]))
            
            else:
                value = int(ligne[i])*2024
                new_ligne.append(f"{value}")
            
        ligne = new_ligne
    return(len(ligne))
                
def arrange_zeros(string):
    if string == '0':
        return string
    elif string[0] != '0':
        return string
    else:
        return arrange_zeros(string[1:])

ligne =['125', '17']

def remplir_dico(p,n, dico):
    a = recursif(p,n, dico)
    dico[(p,n)] = a
    return a
def recursif(p, n, dico):
    if n==0:
        return 1

    if (p, n) in dico.keys():
        return dico[(p,n)]
    if p == '0':
        return remplir_dico('1', n-1, dico)
    
    elif len(p)%2 == 0:
        nP = len(p)

        p1,p2 = int(p[:nP//2]), int(p[nP//2:])
        return remplir_dico(str(p1), n-1, dico) + remplir_dico(str(p2), n-1, dico)
    else:
        return remplir_dico(str(int(p)*2024), n-1, dico)
        
        

def run2(ligne, n):
    dico = {}
    count = 0
    for j in range(len(ligne)):
        pierre = [ligne[j]]

        count += recursif(pierre[0], n, dico)
                    
        
    return count

run2(tableau, 75)



















