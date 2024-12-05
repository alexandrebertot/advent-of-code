
def calcul_distance(fichier="puzzleday1.txt") :
    try: 
        with open(fichier, 'r') as lignes :
            
            data = [int(location) for ligne in lignes for location in ligne.strip().split()]
            location1 = sorted(data[0::2])
            location2 = sorted(data[1::2])
            dist = sum(abs(location1[i] - location2[i]) for i in range (len(location1)))
            return dist
    except FileNotFoundError:
        print(f"Le fichier {fichier} est introuvable")
        return 0
    except ValueError:
        print("Le fichier contient des données non valides.")
        return 0
    

def calcul_similarity(fichier="puzzleday1.txt") :
    try: 
        with open(fichier, 'r') as lignes :
            score = 0
            data = [int(location) for ligne in lignes for location in ligne.strip().split()]
            location1 = data[0::2]
            location2 = data[1::2]
            for location in location1 : 
                score += location * location2.count(location)
            return score
    except FileNotFoundError:
        print(f"Le fichier {fichier} est introuvable")
        return 0
    except ValueError:
        print("Le fichier contient des données non valides.")
        return 0
    
print(calcul_distance("puzzleday1.txt"))
print(calcul_similarity("puzzleday1.txt"))
