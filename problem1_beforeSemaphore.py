import threading
import time
import random

buffer = []
MAX = 10

def producer():
    while True:
        p1 = random.randint(1,100)
        p2 = random.randint(1,100)

        buffer.append(p1)
        print("Produced:", p1)

        time.sleep(0.1)

        buffer.append(p2)
        print("Produced:", p2)

        time.sleep(0.1)

def consumer():
    while True:
        if len(buffer) >= 2:
            p1 = buffer.pop(0)
            p2 = buffer.pop(0)
            print("Consumed pair:", p1, p2)
        else:
            print("Consumer waiting...")

        time.sleep(0.2)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()