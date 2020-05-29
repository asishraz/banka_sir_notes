#wap to enter two numbers and swap their values


a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

''' first way
c = a
a = b
b = c
'''
''' second way
a = a + b
b = a - b
a = a - b

'''

#and the pythonic way
a,b = b,a
print("after swapping")
print(a,b)