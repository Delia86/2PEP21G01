# """Create a class for an object that can:
#  - continually monitor the cpu usage and send send alert when usage is over 50%
#  - get data about de cpu in dictionary format only for keys that have a value
#  -
# """
#
# import os,re
#
# class Cpuchecker:
#     def __init__(self):
#         pass
#
#     def monitor_usage(self):
#         output=str(os.popen("wmic cpu get loadpercentage").readlines())
#         match=re.search(r"\d{1,3}",output)
#         print(match.groups(0))
#         if int(match.group(0))>50:
#             with open("alert.txt","w" ) as alert:
#                 alert.write(f"Your cpu is {match.group(0)}")
#             os.popen("notepad.exe")
#
#     def data(self):
#         output=(str(os.popen("wmic cpu get").readlines()))
#         matches=re.findall(57*r"\w+\s",output)
#         matches2 = re.findall(r"(,\s')(([\S]+\s){1,8}\s+){42}",output)
#         print(matches)
#         dict={}
#         for match in matches[0]:
#             print(match)
#             dict[match]=None
#
#
#
# checker=Cpuchecker()
#
# checker.monitor_usage()
#
#
#
#

#import os
#print(os.listdir())



# List comprehension

my_list=[1,2,3,4,5,6,7,8,9]

squares=[num*num for num in my_list]
print(squares)

# Fibonacci Generator

def fib(num):
    a,b=0,1
    for i in range(0,num):
        yield(f'{i+1}:{a}')
        a,b=b,a+b

for i in fib(10):
    print(i)