#wap to find the sum of first N multiples of an integer K and print it.

K = int(input("enter the number: "))
N = int(input("enter the multiple limit: "))
a = 0


for i in range(1,N+1):
    a += K*i

print(a)