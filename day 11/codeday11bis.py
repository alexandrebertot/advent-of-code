def cut_number(number):
    string = str(number)
    n1 = ''
    n2 = ''
    for i in range(len(string) // 2):
        n1 += string[i]
    for i in range(len(string) // 2, len(string)):
        n2 += string[i]
    return int(n1), int(n2)

blinking = 25
def run(fichier):
    with open(fichier, "r") as f:
        line = f.readline().strip()
        numbers = list(map(int, line.split()))
    new_numbers = []
    for j in range(blinking):
        for i in range(len(numbers)):
            if numbers[i] == 0:
                new_numbers.append(1)

        
            elif len(str(numbers[i])) % 2 == 0:
                    n1, n2 = cut_number(numbers[i])
                    new_numbers.append(n1)
                    new_numbers.append(n2)

        
            else :
                new_numbers.append(numbers[i]*2024)

        numbers = new_numbers
        print(j)
        
    return len(new_numbers)

print(run("test.txt"))

