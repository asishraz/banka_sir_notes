#a leap year is a year which is divisible by 4 ( 1988, 1992)
#but if it is also divisble by 100, then it is not a leap year(1700,1800)
# but if it is also divisible by 400 then it is a leap year  (1600, 2000, 2400)

#wap to enter  a year and print whether it is a leap year or not 


year = int(input("enter the valid year: "))


if year % 4 == 0 and year % 400 == 0:
    print("it is a leap year")
elif year % 4 == 0 and year % 100 == 0:
    print("not a complete leap year")






