def transform(fichier) : 
    with open(fichier, "r") as f:
        ligne = f.readline().strip()
    n = len(ligne)
    blocs = []
    for i in range (n) : 
        len_bloc = int(ligne[i])
        if i%2 == 0 : 
            id = int(i/2)
            for j in range(len_bloc) : 
                blocs.append(id)
        else : 
            for j in range(len_bloc) : 
                blocs.append('.')
    return blocs

def compression(blocs) : 
    n = len(blocs)
    for i in range (n) :
        first_point = blocs.index('.')
        if first_point < n-1-i : 
            blocs[first_point],blocs[n-1-i] = blocs[n-1-i],blocs[first_point]
    return blocs

def get_spaces(blocs) : 
    n = len(blocs)
    space_len = 0
    space_index = 0
    spaces_length = []
    for i in range (n) : 
        if blocs[i] == '.' :
            if space_len == 0 :
                space_index = i
            space_len += 1
            
        else : 
            if space_len > 0 :
                spaces_length.append((space_len,space_index))
                space_len = 0
    return spaces_length



def compression_bis(blocs) : 
    spaces = get_spaces(blocs)
    n = len(blocs)
    viewed = []
    folder_len = 0
    folder_index = 0
    folders = []
    for i in range (n) : 
        if blocs[i] != '.' : 
            if blocs[i] not in viewed : 
                viewed.append(blocs[i])
                if folder_len > 0 : 
                    folders.append((folder_len,folder_index))
                folder_index = i
                folder_len = 1
            else : 
                folder_len += 1
    if folder_len > 0 : 
        folders.append((folder_len,folder_index))
    
    
    m = len(spaces)
    p = len(folders)
    
    for i in range (m) :
        change = False
        print(blocs)
        print(spaces)
        space_index = spaces[i][1]
        

        for j in range (p) : 
        
            if folders[p-j-1][0] <= spaces[i][0] and not change: 
                
                folder_index = folders[p-j-1][1]
                len_f = folders[p-j-1][0]
                for k in range (folders[p-j-1][0]) :
                    blocs[space_index+k],blocs[folder_index+len_f-k-1] = blocs[folder_index+len_f-k-1],blocs[space_index+k]
                spaces = get_spaces(blocs)
                change = True
        
            
        
                

    return blocs


            
        
    
    

def check_sum(compressed_blocs) : 
    sum = 0
    if '.' in compressed_blocs : 
        first_point = compressed_blocs.index('.')
        for i in range (first_point) : 
            sum = sum + i*compressed_blocs[i]
    else : 
        n = len(compressed_blocs)
        for i in range (n) : 
            sum = sum + i*compressed_blocs[i]
    return sum

def check_sum_bis(compressed_blocs) : 
    n = len(compressed_blocs)
    sum = 0
    for i in range(n) : 
        if compressed_blocs[i] != '.' :
            sum = sum + i*compressed_blocs[i]
    return sum



print(transform("test.txt"))
compression_bis(transform("test.txt"))
