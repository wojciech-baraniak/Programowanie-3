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
    with open('in.in') as file:
        data = file.read().split('\n')
    
    for line in data[::]:
        try:
            x = int(line)
        except:
            data.remove(line)
    
    data = [int(x) for x in data]

    with open("plik.txt", "w") as file:
        for num in data:
            if num==1:
                file.write("1\n")
                continue
            string = str(num)+", "

            if pierwsze(num): string += "pierwsze"
            else: string += "zlozone"

            if doskonala(num): string += ", doskonala"

            string += "\n"
            file.write(string)
