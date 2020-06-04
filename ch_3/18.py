#write seperate programs to print the follwing series:
# a) 1,4,9,16,25,36,49,64,81,100
# b) 1,2,4,8,16,32,64,128,256,512,1024
# c) .3, .03, , .003, .0003, .00003, .000003
# d) .3, .33, .333, .3333, .33333, .333333


# for a)

# for i in range(1,11):
#     print(i*i, end=', ')


# for b) 

import math 
from math import pow
# for i in range(0,11):
#     a = math.pow(2,i)
#     print(int(a), end=', ')

#for c)
base_value = 10
main_value = 3
for i in range(1,7):
    a = math.pow(base_value,i)
    print(float(3/a))


#for d)

