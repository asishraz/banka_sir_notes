#wap to input 1000 numbers and print "what a coincidence" if the biggest and smallest, both the numbers are odd

list_of_numbers = [int(input("enter the numbers: ")) for x in range(5)]

small = 0
large = 0

for i in range(len(list_of_numbers)):
    small = list_of_numbers[1]
    if list_of_numbers[i] < small:
        small = list_of_numbers[i]
    elif list_of_numbers[i] > large:
        large = list_of_numbers[i]

if small % 2 != 0 and large % 2 != 0:
    print("What a coincidence!")
