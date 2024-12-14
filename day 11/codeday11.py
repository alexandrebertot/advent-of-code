fichier = "day11.txt"
test = "test.txt"
riad = "riad.txt"

def split_number(nb) : 
    half = int(len(str(nb))/2)
    left_nb = int(str(nb)[0:half])
    right = int(str(nb)[half:])
    return (left_nb,right)

def blink(stones) : 
    n = len(stones) 
    new_stones = []
    for i in range (n) : 
        if stones[i] == 0 : 
            new_stones.append(1)
        elif len(str(stones[i])) % 2 == 0: 
            splited_number = split_number(stones[i])
            new_stones.append(splited_number[0])
            new_stones.append(splited_number[1])
        else : 
            new_stones.append(stones[i]*2024)

    return new_stones

def blinks(fichier,nb_blinks) : 
    with open(fichier, "r") as f:
        line = f.readline().strip()
        stones = list(map(int, line.split()))
    for i in range(nb_blinks) : 
        print(i)
        stones = blink(stones)
    return len(stones)

def blinks_bis(stones,nb) : 
    for i in range (nb) : 
        stones = blink(stones)
    return len(stones)

def rec_blinks(stones,nb) : 
    if len(stones) == 0 :
        return 0
    else : 
        return blinks_bis([stones[0]],nb) +  rec_blinks(stones[1:],nb)


nb_blinks = 75

with open(fichier, "r") as f:
        line = f.readline().strip()
        stones = list(map(int, line.split()))


print(blinks(test,nb_blinks))


