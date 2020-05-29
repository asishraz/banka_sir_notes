#wap to input length in feet and inches and print its equivalent length in metres
# 1ft = 12 inch , 1 inch = 2.54 cm, 100cm = 1m


var_in_ft = int(input("enter the length in ft.: "))
var_in_inch = int(input("enter the lenght in inches: "))

to_inch = var_in_ft * 12 
to_cm = to_inch * 2.54 
to_cm += (var_in_inch * 2.54) 
to_m = (to_cm / 100)


print("length in " + str(var_in_ft) + " ft will be in " + str(to_m) + " metres." )



