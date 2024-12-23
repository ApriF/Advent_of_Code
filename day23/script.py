with open("day23.txt") as fichier:
    data = fichier.readlines()


dico = {}
for ligne in data:
    ligne = ligne.strip()
    key1, key2 = ligne.split("-")

    if key1 not in dico:
        dico[key1] = set()
    dico[key1].add(key2)

    if key2 not in dico:
        dico[key2] = set()
    dico[key2].add(key1)

dico = {key: list(values) for key, values in dico.items()}
#print(dico)
def run():
    count = 0
    for key1 in dico.keys():
        for key2 in dico[key1]:
            for key3 in dico[key2]:
                if key3 in dico[key1] and key1 != key2 and key2 != key3 and key3 != key1 and (key1[0] == 't' or key2[0] == 't' or key3[0] == 't'):
                    count += 1
    return count//6


largest_clique = []

def path_sorted(path):
    for i in range(1, len(path)):
        if path[i-1] > path[i]:
            return False
    return True

i = 0
for start_node in sorted(dico):
    print(i)
    i += 1
    stack = [(start_node, [start_node])]
    while stack:
        current_node, path = stack.pop()
        neighbors = dico[current_node]
        
        for neighbor in sorted(neighbors):
            if path_sorted(path):
                if neighbor == path[0] and len(path) > 2:
                    if all(set(dico[n]) >= set(path) - {n} for n in path):
                        if len(path) > len(largest_clique):
                            largest_clique = path
                    continue
                
    
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))


password = ",".join(sorted(largest_clique))


print(password)

