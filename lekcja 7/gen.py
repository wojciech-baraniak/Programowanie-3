from random import randint, choice
import string

lines = int(input("Ile wygenerować linijek śmieci?: "))
for _ in range(lines):
    t = randint(1,3)
    if t==1:
        print(randint(1, 1000))
    elif t==2:
        print(randint(1,1000)/randint(1,1000))
    else:
        print(''.join(choice(string.ascii_uppercase + string.digits) for _ in range(15)))