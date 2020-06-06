#wap to input a number and print its factors

n = int(input("enter any +ve number: "))
ls = []

for i in range(1,n+1):
    if n % i == 0:
        ls.append(i)

print(ls)