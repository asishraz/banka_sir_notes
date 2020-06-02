#wap to print all the even numbers from A to B 


A = int(input("enter any number: "))
B = int(input("enter any number: "))

for i in range(A,B+1):
    if i%2 == 0:
        print(i)