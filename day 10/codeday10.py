def get_zeros(map) : 
    n = len(map)
    m = len(map[0])
    list_zeros = []
    for i in range (n) : 
        for j in range (m) : 
            if map[i][j] == 0 : 
                list_zeros.append((i,j))
    return list_zeros

def is_in_map(map,coord) :
    n = len(map)
    m = len(map[0])
    if coord[0] >= 0 and coord[1] >= 0 and coord[0] < n and coord[1] < m : 
        return True
    else : 
        return False

def calcul_score(map,list_zeros) : 
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    score = 0
    for i in range(len(list_zeros)) : 
        coord = list_zeros[i]
        nb_reached_nines = 0
        is_trail = True 
        for j in range (9) :
            for move in moves : 
                new_coord = (coord[0] + move[0], coord[1] + move[1])
                if is_in_map(map,new_coord) and map(new_coord) == 
