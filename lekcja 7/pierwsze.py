def pierwsze(n):
    if n<=1: return False

    for i in range(2, n//2+1):
        if not n%i: return False
    return True

def doskonala(n):
    total = []
    if n<=1: return False

    for i in range(1, n//2+1):
        if not n%i: total.append(i)
    
    if sum(total) == n and n>0: return True
    return False

if __name__ == "__main__":
    min = int(input("Podaj minimalna wartosc: "))
    max = int(input("Podaj maksymalna wartosc: "))

    with open("plik.txt", "w") as file:
        for i in range(min, max):
            if i==1:
                file.write("1\n")
                continue
            string = str(i)+", "

            if pierwsze(i): string += "pierwsze"
            else: string += "zlozone"

            if doskonala(i): string += ", doskonala"

            string += "\n"
            file.write(string)
