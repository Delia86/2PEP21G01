# from functools import wraps
#
# def decorator1(func):
#     @wraps(func)
#     def wrapper(*args,** kwargs):
#         return tuple(func(*args,** kwargs))
#     return wrapper
#
# def decorator2(obj_type):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             return obj_type(func(*args, **kwargs))
#         return wrapper
#     return decorator
#
# @decorator1
# @decorator2(str)
# def my_func():
#     print('some_value')
#

# import re
#
# text='Sample'
# pattern=(r'(?P<text>.*)')
# print(re.search(pattern,text).group(0))

# from collections import Counter
#
# class Test(Counter):
#     def __sub__(self,other):
#         for key,value in other.items():
#             self[key]-=value
#
#
# t1=Test('abbccc')
# t2=Test('abc')
# print(t1-t2)

# import matplotlib.pyplot as plt
#
# fig1,(a,b)=plt.subplots(nrows=1,ncols=2,sharex='all')
# a.plot([i for i in range(10)])
# b.plot([1 for i in range(100)])
# plt.show()


# import subprocess
#
# result=subprocess.Popen(['ping','8.8.4.4'],text=True,stderr=subprocess.PIPE)
# result.communicate()

# import asyncio
# import time
#
# async def my_sleep():
#     await asyncio.sleep(1)
#     print('yay')
#
# async def main():
#     await asyncio.wait_for(my_sleep(),timeout=1)
#
# print(asyncio.run(main()))

from multiprocessing import Process,Queue
import time

#
# def f1():
#     time.sleep(1)
#     print('How many times')
#
# if __name__=="__main__":
#     for i in range(10):
#         p=Process(target=f1)
#         p.start()
#         p.join()

q=Queue()

def f1(q):
    q.put(True)
    time.sleep(1)

if __name__=="__main__":
    for i in range(10):
        p=Process(target=f1,args=(q,))
        p.start()
        if q.get():
            p.terminate()