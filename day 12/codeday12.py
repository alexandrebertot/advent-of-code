def is_in_map(map,coord) :
    n = len(map)
    m = len(map[0])
    if coord[0] >= 0 and coord[1] >= 0 and coord[0] < n and coord[1] < m : 
        return True
    else : 
        return False
    
delta = [[1,0],[-1,0],[0,1],[0,-1]]

def cost_field(map, field) : 
    area = len(field)
    perimetre = 0
    n = len(field)
    for i in range(n) :
        list_new_coord = [(field[i][0] + delta[j][0], field[i][1] + delta[j][1]) for j in range (len(delta))]
        for new_coord in list_new_coord :
            if is_in_map(map,new_coord) and map[new_coord[0]][new_coord[1]] != map[field[i][0]][field[i][1]]: 
                perimetre += 1
            if not is_in_map(map,new_coord) : 
                perimetre += 1
    return area*perimetre
    

def get_fields(map):
    n = len(map)
    m = len(map[0])
    viewed = [[False for _ in range(m)] for _ in range(n)]

    def is_in_map(x, y):
        return 0 <= x < n and 0 <= y < m

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y, chara):
        stack = [(x, y)]
        field = []
        while stack:
            coord1, coord2 = stack.pop()
            if not is_in_map(coord1, coord2):
                continue
            if viewed[coord1][coord2] or map[coord1][coord2] != chara:
                continue
            viewed[coord1][coord2] = True
            field.append((coord1, coord2))
            for dx, dy in delta:
                stack.append((coord1 + dx, coord2 + dy))
        return field

    fields = []
    for i in range(n):
        for j in range(m):
            if not viewed[i][j]:
                chara = map[i][j]
                field = dfs(i, j, chara)
                fields.append(field)
    return fields

def calcul_cost(fichier) : 
    with open(fichier, 'r') as f:
        map = [list(line.strip()) for line in f]
    fields = get_fields(map) 
    return sum(cost_field(map,field) for field in fields)
    
print(calcul_cost("day12.txt"))   

with open("test1.txt", 'r') as f:
        map = [list(line.strip()) for line in f]

    
            




