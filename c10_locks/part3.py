# Queue
import time
import threading
from multiprocessing import Queue
from threading import Thread,Event
from time import sleep



def cpu_load(x,queue:Queue):
    start=time.time()
    end=start+2
    while end>time.time():
        x*x
    queue.get()
    start=time.time()
    while not queue.empty():
        sleep(0.1)
    end=time.time()
    print(f'{end-start}{threading.current_thread().getName()}')

# cpu_load(100)

if __name__ =="__main__":
    queue = Queue()
    for i in range(20):
        queue.put(True)
    for i in range(20):
        process=Thread(target=cpu_load,args=(100,queue,))
        process.start()

