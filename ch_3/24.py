#wap to input a number and print its factorial

a = int(input("enter a number: "))
b = 1
if a == 0:
    print("factorial of zero is 1")
for i in range(1,a+1):
    b = b * i

print(b)