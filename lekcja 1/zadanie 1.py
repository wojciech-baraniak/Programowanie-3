from random import randint


class GraLosowanie:
    def __init__(self, min, max):
        self.val = randint(min, max)
        self.t = 1
        self.input = None

    def gra(self):
        while True:
            self.input = int(input("Podaj liczbę: "))
            if self.input == self.val:
                print(f"\033[92mPoprawna lizcba, liczba prób: {self.t}")
                return
            elif self.input > self.val:
                print(f"\033[91mPodana liczba jest za duża, liczba prób: {self.t}")
            elif self.input < self.val:
                print(f"\033[91mPodana liczba jest za mała, liczba prób: {self.t}")

            self.t += 1


gra = GraLosowanie(int(input("Podaj dolny zakres losowania: ")), int(input("Podaj górny zakres losowania: ")))
gra.gra()