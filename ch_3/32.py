# wap to enter a number and print the difference between its factorial and sum of the factors

a = int(input("enter a number: "))

factorial = 1
factors = []
sum_fact = 0

for i in range(1,a+1):
    factorial = factorial * i

for i in range(1,a+1):
    if a%i == 0:
        factors.append(i)

for i in factors:
    sum_fact += i 

diff = factorial - sum_fact
print(factorial)
print(factors)
print(diff)
