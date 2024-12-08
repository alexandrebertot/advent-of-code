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
    for i in range (len(list_antennes)) : 
        for j in range(len(antennes_locations[i])) :
            coord1 = antennes_locations[i][j] 
            for k in range(len(antennes_locations[i])) :  
                if j != k : 
                    coord2 = antennes_locations[i][k]
                    vect = calcul_vector(coord1,coord2)
                    if is_in_map(minus(coord1,vect),n,m) and minus(coord1,vect) not in antinodes_locations : 
                        antinodes_locations.append(minus(coord1,vect))
    return len(antinodes_locations)

def generate_antinodes(fichier )

print(calcul_antinodes("day8.txt"))

            
            

    
