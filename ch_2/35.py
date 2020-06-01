#wap to enter the three digit number  and print whether it is palindrome or not

digit = int(input("enter the four digit number: "))

temp = digit
rev = 0
new_digit = 0

count = 4
#1234

while count > 0:
    rev = digit % 10 #4 
    digit = digit // 10 #123
    new_digit = new_digit * 10 + rev #40
    count -= 1



if temp == new_digit:
    print("palindrome number")

