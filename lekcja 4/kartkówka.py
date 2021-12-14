from math import sqrt

def get_coordinates():
    x1 = int(input("Podaj współrzędną x pierwszego punktu: "))
    y1 = int(input("Podaj współrzędną y pierwszego punktu: "))
    x2 = int(input("Podaj współrzędną x drugiego punktu: "))
    y2 = int(input("Podaj współrzędną y drugiego punktu: "))

    return ((x1, y1), (x2, y2))


def count_distance(coordinates):
    return sqrt(abs((coordinates[0][0] - coordinates[1][0])) ** 2 + abs((coordinates[0][1] - coordinates[1][1])) ** 2)


def main():
    print("To jest program obliczający odległość między dwoma punktami")
    coordinates = get_coordinates()
    distance = count_distance(coordinates)
    print(f"Odległość to: {distance}")


if __name__ == '__main__':
    main()
