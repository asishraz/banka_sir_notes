#wap to input the 1000 numbers and print the biggest and smallest number

list_of_numbers =[int(input("enter the numbers: "))for x in range(5)]

large = 0
small = 0

for i in range(len(list_of_numbers)):
    small = list_of_numbers[1]
    if list_of_numbers[i] < small:
        small = list_of_numbers[i]
    elif list_of_numbers[i] > large:
        large = list_of_numbers[i]

print("the smallest number in the list is: ",small)
print("the largest number in the list is: ",large)