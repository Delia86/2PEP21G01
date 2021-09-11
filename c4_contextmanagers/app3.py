# from app2 import timing
# import matplotlib.pyplot as plt
#
# answer=timing()
# answer1=[0]
# answer2=[1]
#
# fig1,ay1=plt.subplots(nrows=1,ncols=1,sharex='all')
# print(type(ay1))
#
# ay1.plot([i for i in range (1,999)],answer1,answer2,lebel='factorial1 vs factorial2 ')
# ay1.legend()
# plt.xlabel('time')
# plt.ylabel('time2')
# plt.title('factorial')
# plt.show()


from app2 import timing
import matplotlib.pyplot as plt

answer = timing()
answer1 = answer[0]
answer2 = answer[1]


fig1, ay1 = plt.subplots(nrows=1, ncols=1, sharex='all')
print(type(ay1))

ay1.plot([i for i in range(1, 999)], answer1, answer2, label = 'factorial 1 vs factorial 2')
ay1.legend()
plt.xlabel("time")
plt.ylabel('time2')
plt.title("factorial")
plt.show()