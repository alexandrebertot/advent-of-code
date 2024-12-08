import numpy as np

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
    nb_build = 0
    direction_parcours = np.zeros((n,m,4))
    list_build = []
    while pos[0] > 0 and pos[0] < n-1 and pos[1] > 0 and pos[1] < m-1 :
        
        if direction == '<' : 
            if contenu[pos[0]][pos[1]-1] == '.' : 
                contenu[pos[0]][pos[1]-1] = '<'
                contenu[pos[0]][pos[1]] = 'X' 
                pos = (pos[0],pos[1]-1)
                direction_parcours[pos[0]][pos[1]][0] = 1
            elif contenu[pos[0]][pos[1]-1] == '#' :
                contenu[pos[0]][pos[1]] = '^'
                direction = '^'
            else : 
                if direction_parcours[pos[0]][pos[1]-1][1] and pos[1] > 1 :
                    if (pos[0],pos[1]-2) not in list_build : 
                        list_build.append((pos[0],pos[1]-2))
                        nb_build += 1
                contenu[pos[0]][pos[1]-1] = '<'
                direction_parcours[pos[0]][pos[1]][0] = 1
                contenu[pos[0]][pos[1]] = 'X'
                pos = (pos[0],pos[1]-1)
        elif direction == '^' : 
            if contenu[pos[0]-1][pos[1]] == '.' : 
                contenu[pos[0]-1][pos[1]] = '^'
                contenu[pos[0]][pos[1]] = 'X'
                pos = (pos[0]-1,pos[1])
                direction_parcours[pos[0]][pos[1]][1] = 1
            elif contenu[pos[0]-1][pos[1]] == '#' :
                contenu[pos[0]][pos[1]] = '>'
                direction = '>'
            else : 
                if direction_parcours[pos[0]-1][pos[1]][2] and pos[0] > 1 :
                    if (pos[0]-2,pos[1]) not in list_build : 
                        list_build.append((pos[0]-2,pos[1]))
                        nb_build += 1
                contenu[pos[0]-1][pos[1]] = '^'
                direction_parcours[pos[0]][pos[1]][1] = 1
                contenu[pos[0]][pos[1]] = 'X'
                pos = (pos[0]-1,pos[1])
        if direction == '>' : 
            if contenu[pos[0]][pos[1]+1] == '.' : 
                contenu[pos[0]][pos[1]+1] = '>'
                contenu[pos[0]][pos[1]] = 'X' 
                pos = (pos[0],pos[1]+1)
                direction_parcours[pos[0]][pos[1]][2] = 1
            elif contenu[pos[0]][pos[1]+1] == '#' :
                contenu[pos[0]][pos[1]] = 'v'
                direction = 'v'
            else : 
                if direction_parcours[pos[0]][pos[1]+1][3] and pos[1] < m-2 :
                    if (pos[0],pos[1]+2) not in list_build : 
                        list_build.append((pos[0],pos[1]+2))
                        nb_build += 1
                contenu[pos[0]][pos[1]+1] = '>'
                direction_parcours[pos[0]][pos[1]][2] = 1
                contenu[pos[0]][pos[1]] = 'X'
                pos = (pos[0],pos[1]+1)
        elif direction == 'v' : 
            if contenu[pos[0]+1][pos[1]] == '.' : 
                contenu[pos[0]+1][pos[1]] = 'v'
                contenu[pos[0]][pos[1]] = 'X'
                pos = (pos[0]+1,pos[1])
                direction_parcours[pos[0]][pos[1]][3] = 1
            elif contenu[pos[0]+1][pos[1]] == '#' :
                contenu[pos[0]][pos[1]] = '<'
                direction = '<'
            else : 
                if direction_parcours[pos[0]+1][pos[1]][0] and pos[0] < n-2 :
                    if (pos[0]+2,pos[1]) not in list_build : 
                        list_build.append((pos[0]+2,pos[1]))
                        nb_build += 1
                contenu[pos[0]+1][pos[1]] = 'v'
                direction_parcours[pos[0]][pos[1]][0] = 1
                contenu[pos[0]][pos[1]] = 'X'
                pos = (pos[0]+1,pos[1])
                                    
    for k in range(10) : 
        print(list_build[k])              
    return nb_build


print(get_out("day6.txt"))


    