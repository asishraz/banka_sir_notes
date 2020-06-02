#wap to print the sum of all the numbers from A to B

a = 0

A = int(input("enter any number: "))
B = int(input("enter any number: "))

for i in range(A,B+1):
    a = a + i

print(a)