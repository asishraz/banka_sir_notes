#wap to input a number and print its square if it is even else its square root
from math import sqrt

a = int(input("enter the number: "))

if a%2 == 0:
    print("the square of " + str(a) + " is: ", a*a)

elif a%2 != 0:
    print("the square root of " + str(a) + " is :", sqrt(a))

 




