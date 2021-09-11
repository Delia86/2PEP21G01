import logging
import time
from functools import wraps

def my_logg(orig_func):
    logging.basicConfig(filename='log'.format(orig_func.__name__),level=logging.INFO)

    @wraps (orig_func)
    def wrapper(*args,**kwargs):
        logging.info(
            'Ran with args:{},and kwagrs:{}'.format(args,kwargs))
        return orig_func(*args,**kwargs)
    return wrapper

def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=orig_func(*args,**kwargs)
        t2=time.time()-t1
        print('{}ran in: {} sec'.format(orig_func.__name__,t2))
        return result
    return wrapper

@my_logg # using 2 decorators on a single function
@my_timer
def display_info(name, age):
    time.sleep(2)
    print ('display_info ran with args({},{})'.format(name,age))

display_info('Delia',35)

#display()

