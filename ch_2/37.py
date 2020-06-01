#wap to enter two seperate distances in meters and centimeters and print their sum
#10m 25cm + 12m 95cm = 23m 20cm


first_m = int(input("enter the first length in m: "))
first_cm = int(input("enter the first length in cm: "))

second_m = int(input("enter the second length in m: "))
second_cm = int(input("enter the second length in cm: "))


add_m = first_m + second_m
add_cm = first_cm + second_cm

if first_cm < 100 and second_cm < 100:
    if add_cm >= 100:
        add_m += 1
        add_cm = add_cm - 100
        print("total length after calculation is: " +str(add_m) + " m and " + str(add_cm) + " cm")
    elif add_cm < 100:
        print("total length after calculation is: " +str(add_m) + " m and " + str(add_cm) + " cm")






