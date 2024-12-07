def get_pos(fichier = "day6.txt") : 
    with open(fichier,'r') as f :
        contenu = [list(line.strip()) for line in f]

    n = len(contenu)
    for i in range(n) : 
        for j in range(len(contenu[i])) :
            if contenu[i][j] == "^" : 
                return((i,j),"^")
            elif contenu[i][j] == ">" : 
                return((i,j),">")
            elif contenu[i][j] == "v" : 
                return((i,j),"v")
            elif contenu[i][j] == "<" : 
                return((i,j),"<")

def get_out(fichier = "day6.txt") : 
    with open(fichier,'r') as f :
        contenu = [list(line.strip()) for line in f]

    n = len(contenu)
    m = len(contenu[0])
    pos = get_pos(fichier)[0]
    direction = get_pos(fichier)[1] 
    visited = 0
    while pos[0] > 0 and pos[0] < n-1 and pos[1] > 0 and pos[1] < m-1 :
        if direction == '<' : 
            if contenu[pos[0]][pos[1]-1] == '.' : 
                contenu[pos[0]][pos[1]-1] = '<'
                contenu[pos[0]][pos[1]] = 'X'
                visited += 1
                pos = (pos[0],pos[1]-1)
            elif contenu[pos[0]][pos[1]-1] == 'X' :
                contenu[pos[0]][pos[1]-1] = '<'
                contenu[pos[0]][pos[1]] = 'X'
                pos = (pos[0],pos[1]-1)
            else : 
                contenu[pos[0]][pos[1]] = '^'
                direction = '^'
        elif direction == '^' : 
            if contenu[pos[0]-1][pos[1]] == '.' : 
                contenu[pos[0]-1][pos[1]] = '^'
                contenu[pos[0]][pos[1]] = 'X'
                visited += 1
                pos = (pos[0]-1,pos[1])
            elif contenu[pos[0]-1][pos[1]] == 'X' :
                contenu[pos[0]-1][pos[1]] = '^'
                contenu[pos[0]][pos[1]] = 'X'
                pos = (pos[0]-1,pos[1])
            else : 
                contenu[pos[0]][pos[1]] = '>'
                direction = '>'
        elif direction == '>' : 
            if contenu[pos[0]][pos[1]+1] == '.' : 
                contenu[pos[0]][pos[1]+1] = '>'
                contenu[pos[0]][pos[1]] = 'X'
                visited += 1
                pos = (pos[0],pos[1]+1)
            elif contenu[pos[0]][pos[1]+1] == 'X' :
                contenu[pos[0]][pos[1]+1] = '>'
                contenu[pos[0]][pos[1]] = 'X'
                pos = (pos[0],pos[1]+1)
            else : 
                contenu[pos[0]][pos[1]] = 'v'
                direction = 'v'
        elif direction == 'v' : 
            if contenu[pos[0]+1][pos[1]] == '.' : 
                contenu[pos[0]+1][pos[1]] = 'v'
                contenu[pos[0]][pos[1]] = 'X'
                visited += 1
                pos = (pos[0]+1,pos[1])
            elif contenu[pos[0]+1][pos[1]] == 'X' :
                contenu[pos[0]+1][pos[1]] = 'v'
                contenu[pos[0]][pos[1]] = 'X'
                pos = (pos[0]+1,pos[1])
            else : 
                contenu[pos[0]][pos[1]] = '<'
                direction = '<'
        
    visited += 1 #psq on est à la frontière
            
    return visited


print(get_out("day6.txt"))


    