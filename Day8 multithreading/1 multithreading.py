## Multithreading

## when to use multi threading

## I/O bound task: tasks that spend more time waiting for I/o operations (e.g., file operation)

## concurent execution: when you want to improve the throught of your application by performing multiple operations concurrently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

# creating a thread
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)


t = time.time()
# start the thread
t1.start()
t2.start()

# wait for the thread to complete
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)