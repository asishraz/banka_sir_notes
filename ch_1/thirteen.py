#wap to input the sides of a triangle(a,b & c) and calculate its area using the formula given:
#AREA =  Square root of (s*(s-a)*(s-b)*(s-c))
#where s = (a+b+c)/2

from math import sqrt

a = int(input())
b = int(input())
c = int(input())

s = (a+b+c)/2

area = (sqrt(s*(s-a)*(s-b)*(s-c)))


print(area)