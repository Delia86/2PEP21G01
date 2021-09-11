import timeit
import matplotlib.pyplot as plt

numbers= [1,2,3,4,5,6,7,8,9]

s1=f'numbers are:{numbers}'
s2="numbers are:{}".format(numbers)

result1=timeit.timeit('f"numbers are:{[1,2,3,4,5,6,7,8,9]}"')
result2=timeit.timeit('"numbers are{}".format([1,2,3,4,5,6,7,8,9])')

l1,l2= [],[]
def grafic():
    for i in range (100):
        result1=timeit.timeit('f"numbers are:{[1,2,3,4,5,6,7,8,9]}"',number=100)
        l1.append(result1)
        result2 = timeit.timeit('"numbers are{}".format([1,2,3,4,5,6,7,8,9])',number=100)
        l2.append(result2)
    return (l1,l2)

def remove_spikes(y1,y2):
    s1= 0
    s2=0
    for i in range (0,len(y1):
        s1=
        s2=

    for i in range (0,len(y1)):
        if y1[i]

y1,y2=grafic()


fig1,(ay1,ay2)=plt.subplots(nrows=2,ncols=1,sharex='all')
fig1.dpi=200.0
ay1.plot([i for i in range (100)],y1)
ay2.plot ([i for i in range (100)],y1)
plt.show()