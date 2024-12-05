import re

def calcul_sequence(fichier = "day3.txt") :
    with open(fichier,'r') as f :
        contenu = f.read()

    motif = r"mul\((-?\d+),(-?\d+)\)"
    motif_bis = r"do()|don't()"
    res = [(match.group(), match.start()) for match in re.finditer(motif, contenu)]
    resultats = [(match.group(), match.start()) for match in re.finditer(motif_bis, contenu)]
    count = 0
    for sequence in res : 
        i = 0
        if i < len(res) - 1 :
            index = resultats[i+1][1]
            while index < sequence[1] : 
                i += 1
                expr = resultats[i][0]
                index = resultats[i+1][1]
            expr = resultats[i][0]
            print(sequence)
    

    return count

print(calcul_sequence("day3.txt"))
        