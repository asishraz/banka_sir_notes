#wap to enter total marks in five subjects of a student and print the percentage secured by him


sub_1 = int(input())
sub_2 = int(input())
sub_3 = int(input())
sub_4 = int(input())
sub_5 = int(input())


total = sub_1 + sub_2 + sub_3 + sub_4 + sub_5

print(total)

percentage = (total/500) * 100

print(percentage)
