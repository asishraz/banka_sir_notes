#wap to input 1000 numbers and print the smallest number

list_of_numbers = [int(input("enter the numbers: ")) for x in range(5)]

small = 0

for i in range(len(list_of_numbers)):
    small = list_of_numbers[1]
    if list_of_numbers[i] < small:
        small = list_of_numbers[i]

print(small)