from multiprocessing import Process, cpu_count
import time
import os


class MuchCpu(Process):
    def run(self):
        print(f'process id {os.getpid()}')
        for i in range(200_000_000):
            pass


if __name__ == '__main__':
    procs = [MuchCpu() for i in range(cpu_count())]
    print(f'number of procs {len(procs)}')
    start = time.time()
    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()
    print("work took {} seconds".format(time.time() - start))
