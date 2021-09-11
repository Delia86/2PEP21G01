import json
import threading
import time
from multiprocessing import Queue, Barrier, Event
from threading import Thread
import requests

url1 = 'http://worldtimeapi.org/api/timezone/Europe/{}'

url2 = f'http://worldtimeapi.org/api/timezone'

def timezone_getter(q:Queue, location='Europe'):
    response = requests.get(url2)
    my_timezone_str = response.text
    my_timezone = json.loads(my_timezone_str)
    my_list = (list(filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone))))
    for item in my_list:
        q.put(item)

def time_getter(q, barrier:Barrier):
    get = q.get()
    response = requests.get(url1.format(get))
    my_time_str = response.text
    if threading.current_thread().getName()=='Thread-5':
        raise AttributeError
    try:
        barrier.wait()
    except threading.BrokenBarrierError:
        pass
    print(my_time_str)
    return json.loads(my_time_str)

def excepthook(args,/):
    with open ('errorlog.txt','w')as file:
        file.write(f'{args.thread.getName()} failed with{args.exc_type}')

threading.excepthook=excepthook


if __name__ == '__main__':
    queue = Queue()
    th1 = Thread(target=timezone_getter, args=(queue, 'Europe'))
    th1.start()

    barrier = Barrier(10, timeout=10)
    p_list=[]
    for i in range(10):
        th = Thread(target=time_getter, args=(queue,barrier ))
        p_list.append(th)
    for th in p_list:
        th.start()
    for th in p_list:
        print (type(th.join()))
