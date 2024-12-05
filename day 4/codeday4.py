def look_re(fichier = "day4.txt") : 
    with open(fichier,'r') as contenu :
        f = [line.strip() for line in contenu.readlines()]
    n = len(f)
    nb_occ = 0
    for j in range (n) : 
        
        m = len(f[j])
        for i in range(m) : 
            if f[j][i] == "X" : 
                #recherche par ligne 
                if i < m-3 and f[j][i+1] == "M" and f[j][i+2] == "A" and f[j][i+3] == "S" : 
                    nb_occ += 1
                    
                    
                if i > 2 and f[j][i-1] == "M" and f[j][i-2] == "A" and f[j][i-3] == "S" : 
                    nb_occ += 1
                    
                    
                #recherche par colonne 
                if j < n-3 and f[j+1][i] == "M" and f[j+2][i] == "A" and f[j+3][i] == "S" : 
                    nb_occ += 1
                if j > 2 and f[j-1][i] == "M" and f[j-2][i] == "A" and f[j-3][i] == "S" :
                    nb_occ += 1
                #recherche diago par le bas 
                if j < n-3 :
                    if i < m-3 and f[j+1][i+1] == "M" and f[j+2][i+2] == "A" and f[j+3][i+3] == "S" :
                        nb_occ += 1
                        
                    if i > 2 and f[j+1][i-1] == "M" and f[j+2][i-2] == "A" and f[j+3][i-3] == "S" : 
                        nb_occ += 1 
                    
                #recherche diago vers le haut
                if j > 2 :
                    if i < m-3 and f[j-1][i+1] == "M" and f[j-2][i+2] == "A" and f[j-3][i+3] == "S" :
                        nb_occ += 1
                       
                    if i > 2 and f[j-1][i-1] == "M" and f[j-2][i-2] == "A" and f[j-3][i-3] == "S" : 
                        nb_occ += 1 
                        
    return nb_occ

def look_re_bis(fichier="day4.txt"):
    
    with open(fichier, 'r') as contenu:
        f = [line.strip() for line in contenu.readlines()]
    
    n = len(f)  
    nb_occ = 0

    
    delta = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

    for j in range(n):  
        m = len(f[j])  
        for i in range(m):  
            if f[j][i] == "A" and 0 < i < m - 1 and 0 < j < n - 1:
                
                try:
                    
                    pos0 = (j + delta[0][0], i + delta[0][1])
                    pos1 = (j + delta[1][0], i + delta[1][1])
                    pos2 = (j + delta[2][0], i + delta[2][1])
                    pos3 = (j + delta[3][0], i + delta[3][1])

                    
                    if (
                        f[pos0[0]][pos0[1]] == f[pos1[0]][pos1[1]] == "M" and
                        f[pos2[0]][pos2[1]] == f[pos3[0]][pos3[1]] == "S"
                    ):
                        nb_occ += 1
                    if (
                        f[pos0[0]][pos0[1]] == f[pos1[0]][pos1[1]] == "S" and
                        f[pos2[0]][pos2[1]] == f[pos3[0]][pos3[1]] == "M"
                    ):
                        nb_occ += 1
                    if (
                        f[pos0[0]][pos0[1]] == f[pos2[0]][pos2[1]] == "M" and
                        f[pos1[0]][pos1[1]] == f[pos3[0]][pos3[1]] == "S"
                    ):
                        nb_occ += 1
                    if (
                        f[pos0[0]][pos0[1]] == f[pos2[0]][pos2[1]] == "S" and
                        f[pos1[0]][pos1[1]] == f[pos3[0]][pos3[1]] == "M"
                    ):
                        nb_occ += 1
                except IndexError:

                    continue

    return nb_occ


print(look_re_bis("day4.txt"))




