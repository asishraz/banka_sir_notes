#q 21 - 26, I haven't touched, will do it later

#wap to enter angles of triangle and print its type as acute, obtuse or right angled

first_angle = int(input("enter the first angle: "))
second_angle = int(input("enter the second angle: "))
third_angle = int(input("enter the third angle: "))


if first_angle < 90:
    print(str(first_angle) + " is acute angle")
elif first_angle > 90 and first_angle < 180:
    print(str(first_angle) + " is obtuse angle")
elif first_angle == 90:
    print(str(first_angle) + " is right angle")

if second_angle < 90:
    print(str(second_angle) + " is acute angle")
elif second_angle > 90 and second_angle < 180:
    print(str(second_angle) + " is obtuse angle")
elif second_angle == 90:
    print(str(second_angle) + " is right angle")

if third_angle < 90:
    print(str(third_angle) + " is acute angle")
elif third_angle > 90 and third_angle < 180:
    print(str(third_angle) + " is obtuse angle")
elif third_angle == 90:
    print(str(third_angle) + " is right angle")