import re

with open("day3.txt") as fichier:
    contenu = fichier.read()
    

def do(contenu):
    # Pattern trouvé avec le chat
    instruction_pattern = r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))"

    mul_enabled = True  
    tot = 0

    matches = re.finditer(instruction_pattern, contenu)
    
    for match in matches:
        if match.group(1):
            if mul_enabled:
                x, y = int(match.group(2)), int(match.group(3))
                tot += x * y
        elif match.group(4):
            mul_enabled = True
        elif match.group(5):
            mul_enabled = False
    
    return tot

do(contenu)