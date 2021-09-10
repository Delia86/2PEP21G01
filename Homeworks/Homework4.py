""" Create a context manager that will time how long it took to execute the context and display a graph with
execution time when the context ends.
Since the same instance can be used in multiple contexts make sure that the graph will show data for each time the
object was used in a context
example
obj = Obj()
with obj as value1:
    ...
with obj as value2:
    ...
Now graph will contain 2 values
"""

from contextlib import contextmanager

import matplotlib.pyplot as plt
import time


a,b=[],[]

@contextmanager
def timing():

    start = time.time()
    yield
    end_time = time.time() - start

    print(f" {end_time}")
    fig1,(a,b) = plt.subplots(nrows=2, ncols=1, sharex='all')
    plt.plot(a,b)



with timing():
    s = [x for x in range(10_000_000)]