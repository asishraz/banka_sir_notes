#wap to enter two seperate distances in feet and inches and print their sum
#e.g 4ft 10 in + 5ft 6in = 10ft 4 inch

first_ft = int(input("enter the first length in ft: "))
first_in = int(input("enter the first length in inch: "))

second_ft = int(input("enter the second length in ft: "))
second_in = int(input("enter the second length in inch: "))

add_ft = first_ft + second_ft
add_in = first_in + second_in

if first_in < 12 and second_in < 12:
    if add_in >= 12:
        add_ft += 1
        add_in = add_in - 12
        print("total length after calculation is: " +str(add_ft) + " ft and " + str(add_in) + " inch")
    elif add_in < 12:
        print("total length after calculation is: " +str(add_ft) + " ft and " + str(add_in) + " inch")
