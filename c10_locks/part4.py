# Barrier

import time
import threading
from multiprocessing import Queue
from threading import Thread,Event,Barrier
from time import sleep
import random



def cpu_load(x,barrier:Barrier):
    start=time.time()
    end=start+ random.randint(1,10)
    while end>time.time():
        x*x
    start = time.time()
    barrier.wait()
    end=time.time()
    print(f'{end-start}{threading.current_thread().getName()}')

# cpu_load(100)

if __name__ =="__main__":
    barrier=Barrier(20)
    for i in range(20):
        process=Thread(target=cpu_load,args=(100,barrier))
        process.start()

