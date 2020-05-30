#wap to input marks in 5 subjects of a candidate and print his or her percentage and grade

# 80% and above  grade A
# 60% to less than 80% - grade B
# 40% to less than 60% - grade C
# below 40% - grade D


a = int(input("enter the first marks: "))
b = int(input("enter the second marks: "))
c = int(input("enter the third marks: "))
d = int(input("enter the forth marks: "))
e = int(input("enter the fifth marks: "))

scored = a + b + c + d + e

total_marks = 500

percentage = (scored / total_marks) * 100

if percentage >= 80:
    print("total percent: " +str(percentage) + " % and Grade A")
elif percentage < 80 and percentage >= 60:
    print("total percent: " + str(percentage) + " % and Grade B")
elif percentage < 60 and percentage >= 40:
    print("total percent: " + str(percentage) + " % and Grade C")
else:
    print("total percent: " + str(percentage) + " % and Grade D")