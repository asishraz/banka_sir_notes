#wap to enter the three angles of a triangle and check the validity of the triangle


first_angle = int(input("enter the first angle: "))
second_angle = int(input("enter the second angle: "))
third_angle = int(input("enter the third angle: "))


#validity rule :- sum of angles = 180

if first_angle + second_angle + third_angle == 180:
    print("valid triangle")

