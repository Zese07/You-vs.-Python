import random
import threading
import os
import sys

def math(m):
    global n1, n2, c, o, f
    n1 = random.randint(1, 25 * m)
    n2 = random.randint(1, 25 * m)
    n = random.randint(1, 4)

    match n:
        case 1:
            c = n1 + n2
            o = '+'
        case 2:
            c = n1 - n2
            o = '-'
        case 3:
            c = n1 * n2
            o = '*'
        case 4:
            c = n1 / n2
            o = '/'
        case _:
            print('Error')

    f = c
    if f <= -1:
        f *= -1

    while f >= 10:
        f /= 10

def remove():
    print('You got bitten by the Python.')
    os.remove(os.path.basename(sys.argv[0]))
    exit()

def dead():
    if os.path.exists("="):
        os.rmdir("=")

    if os.path.exists("=.txt"):
        os.remove("=.txt")

    if os.path.exists("=.py"):
        os.remove("=.py")

    match int(f):
        case 0:
            if os.path.exists(str(c)):
                print('You managed to escape the Python.')
                exit()
            else:
                remove()

        case 1 | 2 | 3 | 4 | 5:
            if os.path.exists(str(c) + ".txt"):
                print('You managed to escape the Python.')
                exit()
            else:
                remove()

        case 6 | 7 | 8 | 9:
            if os.path.exists(str(c) + ".py"):
                print('You managed to escape the Python.')
                exit()
            else:
                remove()

        case _:
            print('Error')

def files():
    if os.path.exists("="):
        os.rmdir("=")
    else:
        os.makedirs("=")

    if os.path.exists("=.txt"):
        os.remove("=.txt")
    else:
        open("=.txt", "x")

    if os.path.exists("=.py"):
        os.remove("=.py")
    else:
        open("=.py", "x")

def timer():
    global t
    c = random.randint(1, 4)
    t = 15.0 * c
    threading.Timer(t, dead).start()
    math(c)
    files()

timer()

print('Python started a: ' + str(t) + ' seconds timer.')
print('Python asked what is: ' + str(n1) + ' ' + o + ' ' + str(n2) + ' = ?')
print('Rename the = before the Python attacks you.')
