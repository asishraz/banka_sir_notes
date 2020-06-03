#wap to input 20 numbers and print the sum of numbers and the numbers that are greater than 100

user_input = [int(input("enter the number: ")) for x in range(5)]

for i in user_input:
    if i + (i + 1) > 100:
        print(i)
    elif i > 100:
        print(i)