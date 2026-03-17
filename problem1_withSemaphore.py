import threading
import time
import random

buffer = []
BUFFER_SIZE = 10

empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)

def producer():
    while True:
        p1 = random.randint(1,100)
        p2 = random.randint(1,100)

        empty.acquire()
        empty.acquire()

        mutex.acquire()
        buffer.append(p1)
        buffer.append(p2)
        print("Produced pair:", p1, p2)
        mutex.release()

        full.release()
        full.release()

        time.sleep(0.2)

def consumer():
    while True:
        full.acquire()
        full.acquire()

        mutex.acquire()
        p1 = buffer.pop(0)
        p2 = buffer.pop(0)
        print("Consumed pair:", p1, p2)
        mutex.release()

        empty.release()
        empty.release()

        time.sleep(0.3)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()