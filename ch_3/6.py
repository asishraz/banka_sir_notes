#wap to print the sum of all the even numbers from A to B
# 
A = int(input("enter any number: "))
B = int(input("enter any number: "))

a = 0

for i in range(A,B+1):
    if i % 2 == 0:
        a = a + i

print(a)