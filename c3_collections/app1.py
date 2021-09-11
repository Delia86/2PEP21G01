"Create a string like object that is capable of determining if information is transmited in a sample of test "

from collections import Counter,UserString

class InformationGetter(UserString):

    def information (self):
        my_data= Counter(self.split())
        for key in my_data.keys():
            if len(key)<=3:
                my_data[key]-=my_data[key]
        print(my_data)
        sum=0
        for value in my_data.values():
            sum=sum+value
        average=sum/len(my_data.keys())
        maxdeviation=average*(200/100)

        for key in my_data.keys():
            if my_data[key] <maxdeviation:
                print(key)

with open('my_data') as f:
    my_data= f.read()

getter=InformationGetter(my_data)
getter.information()


# from collections import Counter
# def read_write(file):
#     with open(file) as f:
#         my_file =
# f.read
# ()
#     c = Counter()
#     for i in my_file.split():
#         c[i] += 1
#     print(c)
# read_write('my_data')