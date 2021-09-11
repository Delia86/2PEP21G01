# Event
import time
import threading
from threading import Thread,Lock,Event

def cpu_load(x,event:Event):
    start=time.time()
    end=start+2
    while end>time.time():
        x*x
    event.wait()
    event.clear()
    print(f'{threading.current_thread().getName()}')
    event.set()

# cpu_load(100)

if __name__ =="__main__":
    event=Event()
    event.set()
    for i in range(20):
        process=Thread(target=cpu_load,args=(100,event,))
        process.start()

