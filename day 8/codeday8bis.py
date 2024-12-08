def get_antennes (map) : 
    n = len(map)
    m = len(map[0])
    list_antennes = []
    antennes_locations = []
    nb_antennes = 0
    for i in range (n) : 
        for j in range(m) : 
            if map[i][j] != '.' : 
                if map[i][j] not in list_antennes : 
                    list_antennes.append(map[i][j])
                    antennes_locations.append([])
                    antennes_locations[nb_antennes].append((i,j))
                    nb_antennes += 1
                    
                else : 
                    k = list_antennes.index(map[i][j])
                    antennes_locations[k].append((i,j))
                    
    return (list_antennes,antennes_locations)

def calcul_vector(coord1,coord2) : 
    return (coord2[0]-coord1[0],coord2[1]-coord1[1])

def minus(coord,vector) : 
    return (coord[0]-vector[0],coord[1]-vector[1])

def is_in_map(coord,n,m) :
    if coord[0] >=0 and coord[0] < n and coord[1] >=0 and coord[1] < m : 
        return True
    else : 
        return False

def calcul_antinodes(fichier = "day8.txt") : 
    with open(fichier,'r') as f :
        map = [list(line.strip()) for line in f]
    n = len(map)
    m = len(map[0])
    list_antennes, antennes_locations = get_antennes(map)
    
    antinodes_locations = []
    only_antinodes = []

    for b in range(len(list_antennes)) :
        if len(antennes_locations[b]) > 1 : 
            for p in range (len(antennes_locations[b])) : 
                antinodes_locations.append(antennes_locations[b][p])
    for i in range (len(list_antennes)) : 
        for j in range(len(antennes_locations[i])) :
            coord1 = antennes_locations[i][j] 
            for k in range(len(antennes_locations[i])) :  
                if j != k : 
                    coord2 = antennes_locations[i][k]
                    vect = calcul_vector(coord1,coord2)
                    new_vect = vect
                    while is_in_map(minus(coord1,new_vect),n,m) :
                        if minus(coord1,new_vect) not in antinodes_locations : 
                            antinodes_locations.append(minus(coord1,new_vect))
                            only_antinodes.append(minus(coord1,new_vect))
                        new_vect = (new_vect[0] + vect[0], new_vect[1] + vect[1])

    return len(antinodes_locations)
'''
def create_map_antinodes(fichier, antinode_locations, map_with_antinodes):
    with open(fichier, 'r') as f: 
        map = [list(line.strip()) for line in f]
    
    for coord in antinode_locations: 
        x, y = coord
        map[x][y] = '#' 
    
    with open(map_with_antinodes, 'w') as f: 
        for line in map : 
            f.write(''.join(line) + '\n')

fichier = "test.txt"
antinode_locations = calcul_antinodes("test.txt")
maps = "carte.txt"

create_map_antinodes(fichier,antinode_locations,maps)
'''


print(calcul_antinodes("day8.txt"))
    

    
