import threading

def p1():
    while True:
        print("H", end="")
        print("E", end="")

def p2():
    while True:
        print("L", end="")

def p3():
    while True:
        print("O", end="")

threading.Thread(target=p1).start()
threading.Thread(target=p2).start()
threading.Thread(target=p3).start()