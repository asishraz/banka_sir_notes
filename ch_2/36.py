#wap to enter two three digits number and print if the middle digit of both the numbers is same

a = int(input("enter 3-digit number: "))
temp_a = a
b = int(input("enter 3-digit number: "))
temp_b = b

count = 2
#a = 123
#b = 324

while count > 0 :
    rev_a = a % 10 #3 #2
    a = a // 10 #12
    rev_b = b % 10
    b = b // 10
    count -= 1

if rev_a == rev_b:
    print("the middle digit of " + str(temp_a) + " and " + str(temp_b) + " are same")

