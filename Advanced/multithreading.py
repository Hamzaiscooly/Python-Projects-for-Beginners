# Multithreading Example

import threading

def print_numbers():
    for i in range(5):
        print("Number", i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()