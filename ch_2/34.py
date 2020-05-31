#wap to enter the three digit number  and print whether it is palindrome or not

digit = int(input("enter the three digit number: "))
temp = digit

count = 3
new_digit = 0
rev = 0

#456

while count > 0:
    rev = digit % 10  #4
    digit = digit // 10 #0
    new_digit = new_digit * 10 + rev  #65
    count -= 1
    
if temp == new_digit:
    print("palindrome number")


