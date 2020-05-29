#wap to input marks out of 800 and print "pass" if it is greater than 50% otherwise print "fail"


marks = int(input("enter the marks out of 800: "))

if marks > (50/100) * 800:
    print("pass")
else:
    print("fail")