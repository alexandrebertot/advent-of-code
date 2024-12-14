import numpy as np
import re
constant = 10000000000000
def solve_equation(X,Y,b) : 
    A = np.array([[X[0], Y[0]],[X[1], Y[1]]])
    sol = np.linalg.solve(A, b)
    n, m = sol
    return (n,m)

def is_int(value, epsilon = 1e-3) : 
    if abs(value - round(value)) < epsilon : 
        return True 
    else : 
        return False
    
def tokens(fichier) : 
    with open (fichier, "r") as f : 
        machines = f.readlines()
    n = len(machines)
    nb_tokens = 0
    for i in range (n) : 
        if i % 4 == 0 : 
            numbers = re.findall(r'\d+', machines[i])
            X = [int(number) for number in numbers]
            
            numbers = re.findall(r'\d+', machines[i+1])
            Y = [int(number) for number in numbers]

            numbers = re.findall(r'\d+', machines[i+2])
            b = [constant + int(number) for number in numbers]

            (p,q) = solve_equation(X,Y,b)
            if is_int(p) and is_int(q) :
                nb_tokens = nb_tokens + 3*round(p) + round(q)

    return nb_tokens


print(tokens("day13.txt"))


X = [94, 34]
Y = [22, 67]
b = [8400, 5400]

(n,m) = solve_equation(X,Y,b)

print(isinstance(n,int))
