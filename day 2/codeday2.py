def is_safe(liste) : 
    n = len(liste)
    if n > 1 :
        for i in range(n-1) : 
            if liste[0] > liste[1] : #decreasing list
                if liste[i] <= liste [i+1] :
                    return False
                if liste[i] - liste[i+1] > 3 : 
                    return False
            if liste[0] < liste[1] : #decreasing list
                if liste[i] >= liste[i+1] : 
                    return False
                if liste[i] - liste[i+1] < -3 :
                    return False
            if liste[0] == liste[1] : 
                return False
    return True

def is_safe_bis(liste) :
    if is_safe(liste) == False : 
        n = len(liste)
        for i in range(n) : 
            if i == n-1:
                new_liste = liste[:i]
                if is_safe(new_liste):
                    return True
            else : 
                new_liste = liste[:i] + liste[i+1:]
                if is_safe(new_liste):
                    return True
        return False
    return True

                


                    
        



def number_of_safe(fichier="day2.txt") : 
    try : 
        with open(fichier, 'r') as lignes :
            nb_safe = 0
            for ligne in lignes :
                l = ligne.strip().split()
                l_bis = [int(elem) for elem in l]
                if is_safe_bis(l_bis) : 
                    print(l_bis)
                    nb_safe += 1
                
            return nb_safe
    except FileNotFoundError:
        print(f"Le fichier {fichier} est introuvable")
        return 0
    except ValueError:
        print("Le fichier contient des données non valides.")
        return 0



print(number_of_safe("day2.txt"))
