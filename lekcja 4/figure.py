from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        if self.a<=0 or self.b<=0 or self.c<=0: raise ValueError('Triangle does not exist')
        if self.a+self.b <= self.c: raise ValueError('Triangle does not exist')
        if self.b+self.c <= self.a: raise ValueError('Triangle does not exist')
        if self.a+self.c <= self.b: raise ValueError('Triangle does not exist')

    @property
    def length(self):
        return self.a+self.b+self.c

    @property
    def area(self):
        p = 0.5*self.length
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

if __name__ == "__main__":
    t = Triangle(1, 3, 3)
    print(t.area)
