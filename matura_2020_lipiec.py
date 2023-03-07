class matura_2020_lipiec:
    def __init__(self):
        pass
    def zadanie4_1(self):
        l = [x.strip() for x in open('identyfikator.txt', 'r')]
        odp = []
        for i in l:
            x = i[3:]
            s = 0
            for j in x:
                s += int(j)
            odp.append(s)
        max = max(odp)

        for i in range(len(l)):
            if odp[i] == max:
                print(l[i])
        print()
    def zadanie4_2(self):
        l = [x.strip() for x in open('identyfikator.txt', 'r')]

        for i in l:
            s = i[:3]
            n1 = i[3:6]
            n2 = i[6:]

            flag = True
            for j in range(3):
                if n1[j] != n2[2 - j]:
                    flag = False
                    break
            if s[0] == s[2] or flag:
                print(i)

        print()
    def zadanie4_3(self):
        l = [x.strip() for x in open('identyfikator.txt', 'r')]

        for q in l:

            a = ord(q[0]) - 55
            b = ord(q[1]) - 55
            c = ord(q[2]) - 55

            e = int(q[4])
            f = int(q[5])
            g = int(q[6])
            h = int(q[7])
            i = int(q[8])
            kon = e * 7 + f * 3 + g + h * 7 + i * 3
            t = a * 7 + b * 3 + c
            kon += t
            kon = kon % 10
            k = int(q[3])
            if k != kon:
                print(q)
