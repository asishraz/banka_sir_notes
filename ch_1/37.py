#wap to enter a four digit number and print it in reverse order


digit = int(input("enter the four digit number: "))

#1234

count = 4
rev = 0
add = 0


while count > 0:
    rev = digit % 10 #4
    digit = digit // 10 #123
    add = add * 10 + rev #4
    count -= 1

print(add)
