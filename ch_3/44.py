#wap to print the perfect numbers between A and B

# A = int(input("enter the number: "))
# B = int(input("enter the number: "))

# N = int(input("enter the range: "))


'''
6 => 1+2+3 = 6(sum of factors equals the number)
'''

# fact = 0
# for i in range(1,N):
#     if N%i == 0:
#         fact += i
        

# if fact == N:
#     print(str(N) + " is a perfect number")

def perfect_number(a,b):
    fact_a = 0
    fact_b = 0
    for j in range(1,a):
        if a%j == 0:
            fact_a += j
    for k in range(1,b):
        if b%k == 0:
            fact_b += k

    if fact_a == a:
        print(str(a) + " is a perfect number")
    elif fact_b == b:
        print(str(b) + " is a perfect number")



var = perfect_number(2,10)
print(var)