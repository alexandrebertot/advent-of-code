import re

def is_rule(a,b,list_rules) : 
    if (a,b) in list_rules : 
        return True
    else :
        return False

def is_correct_update(upd,list_rules) : 
    n = len(upd)

    for i in range(n) : 
        for j in range(i+1,n) : 
            if is_rule(upd[i],upd[j],list_rules) :
                continue
            else : 
                return False
    return True

def get_update(fichier = "day5.txt") : 
    with open(fichier,'r') as f :
        contenu = f.read()
    count = 0
    lignes = contenu.splitlines()
    n = len(lignes)
    motif = r"\d+\|\d+"
    resultats = re.findall(motif, contenu)
    list_rules = []
    for element in resultats : 
        left_side, right_side = element.split('|')
        left_int = int(left_side)
        right_int = int(right_side)
        new_rule = (left_int,right_int)
        list_rules.append(new_rule)
    
    last_index = -1
    for ligne in lignes : 
        if '|' in ligne : 
            last_index += 1
    m = last_index + 2 #ligne à partir d'où commence la deuxième partie
    
    for j in range(m,n) : 
        ligne = lignes[j].split(',')
        upd = [int(x) for x in ligne]
        mid = int((len(upd) - 1)/2)
        if is_correct_update(upd,list_rules) : 
            
            count = count + upd[mid]
    
    return count

def correct_update(upd,list_rules) : 
    n = len(upd) 
    for i in range(n) : 
        for j in range(i+1,n) :
            if is_rule(upd[j],upd[i],list_rules) and upd[i] != upd[j] : 
                upd[i],upd[j] = upd[j],upd[i]
    return upd



def get_update_bis(fichier = "day5.txt") : 
    with open(fichier,'r') as f :
        contenu = f.read()
    count = 0
    lignes = contenu.splitlines()
    n = len(lignes)
    motif = r"\d+\|\d+"
    resultats = re.findall(motif, contenu)
    list_rules = []
    for element in resultats : 
        left_side, right_side = element.split('|')
        left_int = int(left_side)
        right_int = int(right_side)
        new_rule = (left_int,right_int)
        list_rules.append(new_rule)
    
    last_index = -1
    for ligne in lignes : 
        if '|' in ligne : 
            last_index += 1
    m = last_index + 2 #ligne à partir d'où commence la deuxième partie
    
    for j in range(m,n) : 
        ligne = lignes[j].split(',')
        upd = [int(x) for x in ligne]
        mid = int((len(upd) - 1)/2)
        if not is_correct_update(upd,list_rules) : 
            upd = correct_update(upd,list_rules)
            
            count = count + upd[mid]
    
    return count
        
print(get_update("day5.txt"))
print(get_update_bis("day5.txt"))
    


