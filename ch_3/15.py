#wap to print the table of N (upto Z times)

N = int(input("enter the number for the table: "))

Z = int(input("enter the number of times: "))

for i in range(1,Z+1):
    print(i*N)