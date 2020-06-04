#wap to print the product of all the numbers from 1 to N

N = int(input("enter any number: "))
a = 1
for i in range(1,N+1):
    a = a * i

print(a)
