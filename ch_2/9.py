#wap to input three numbers and print the smaller number

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))



if a < b and a < c:
    print(str(a) + " is smaller")
elif b < c and b < a:
    print(str(b) + " is smaller")
else:
    print(str(c) + " is smaller")