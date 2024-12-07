import itertools

def concatenation(a,b) : 
    return int(str(a)+str(b))


def check_equation(equation) : 
    resultat = equation[0]
    values = equation[1:]
    n = len(values)
    list_operators = list(itertools.product([0,1,2], repeat = n-1)) #liste des opérateurs avec 0 = + et 1 = * et 2 = concaténation
    for operators in list_operators : 
        s = 0
        for j in range (n-1) : 
            if operators[j] == 0 : 
                if j == 0 : 
                    s = values[j] + values[j+1]
                else : 
                    s = s + values[j+1]
            elif operators[j] == 1 : 
                if j == 0 : 
                    s = values[j] *  values[j+1]
                else : 
                    s = s * values[j+1]
            else : 
                if j == 0 : 
                    s = concatenation(values[j],values[j+1])
                else : 
                    s = concatenation(s,values[j+1])
        if resultat == s : 
            return True
    return False
                    

def get_sum_equations(fichier = "day5.txt") : 
    with open(fichier,'r') as f :
        contenu = f.read()
    count = 0
    lignes = contenu.splitlines()
    for ligne in lignes : 
        equation = [int(x) for x in ligne.replace(":","").split()]
        if check_equation(equation) : 
            count = count + equation[0]
    return count

print(get_sum_equations("day7.txt"))