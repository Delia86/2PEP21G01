"""some docstring"""

import time

# pylint:disable= unused-argument
def my_sleep(val:int):
    """ some doctring"""
    print('before sleep')
    try:
        time.sleep(val)
    except Exception:
        print('something happened')
    finally:
        pass
    print('after sleep')