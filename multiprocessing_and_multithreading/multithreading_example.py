from threading import Thread
from multiprocessing import cpu_count
import time
import os


class MuchCpu(Thread):
    def run(self):
        print(f'process id {os.getpid()}')
        for i in range(200_000_000):
            pass


if __name__ == '__main__':
    threads = [MuchCpu() for i in range(cpu_count())]
    print(f'number of procs {len(threads)}')
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("work took {} seconds".format(time.time() - start))
