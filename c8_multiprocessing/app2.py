import json
import requests
import time
from multiprocessing import Process, Queue, Pipe
import random
import os

def generate_numbers(q):
    for i in range(10):
        q.put(random.randint(0,500))
        time.sleep(1)

def raise_to_power(q,p):
    x=q.get()
    print(f'{os.getpid()}processing for one sec')
    time.sleep(1)
    p[0].send(x*x)
    time.sleep(3)
    p[0].close()

if __name__ == '__main__':
    q=Queue()
    p=Pipe()
    list1=[]
    process1=Process(target=generate_numbers,args=(q,))
    process_list=[process1]
    for i in range(3):
        process=Process(target=raise_to_power, args=(q,p,))
        process_list.append(process)
    for process in process_list:
        process.start()
    time.sleep(0.1)
    print(p[1].recv())
    for process in process_list:
        print(type(process.join()))

