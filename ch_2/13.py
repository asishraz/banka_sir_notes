#wap to enter the three sides of a triangle and check for the validity of the triangle
#validity rule :_ the sum of any two sides of the triangle is always greater than the third side 


first_side = int(input("enter the first side of the triangle: "))
second_side = int(input("enter the second side of the triangle: "))
third_side = int(input("enter the third side of the triangle: "))


if first_side + second_side > third_side:
    print("a valid triangle")
elif second_side + third_side > first_side:
    print("a valid triangle")
elif third_side + first_side > second_side:
    print("a valid triangle")
else:
    print("not a valid triangle")
