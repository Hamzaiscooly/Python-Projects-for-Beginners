# Multiprocessing Example

import multiprocessing

def worker():
    print("Worker process")

if __name__ == "__main__":
    process = multiprocessing.Process(target=worker)
    process.start()
    process.join()