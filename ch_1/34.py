#wap to enter the number of days and convert it into years, months, weeks and days.
# #e.g 452 days equals 1yr, 2mnths, 3 weeks and 6 days
# Assume 365 days in a year and 30 days  in a month 


num_of_days = int(input("enter the number of days: "))


#first check whether the num-of_days is less than 365 or not  , e.g 100
# if num_of_days < 365:
# if yes, then we can directly divide the number with 30
# int(100/30) = 3 => this will be number of months 
#then we have to see the remainder and that will change into weeks or days
# int(100%30) = 10 => 10 number of days
#now see, if 10 is less than 7 or not for the week and days calculation
#if yes, then we can say directly the number of days
#and if not, then divide it by 7 to get the number of weeks and the days
#int(10/7) => 1 week and then we will see the remainder, which will determine the numnber of days
#int(10%7) => 3, this is the number of days


#in case, the number of days is greater than 365, e.g 400
#first divide the number of days with 365, in order to find the number of years first
#int(400/365) => 1 , this will be the number of years
#now see the remainder and do the above part again and find the number of months , weeks and days

for_years = 0
for_months = 0
days_left = 0
for_week = 0
for_days = 0

if num_of_days < 365:
    for_years = 0
    for_months = int(num_of_days/30)
    days_left = int(num_of_days%30)
    if days_left < 7:
        for_days = days_left
    elif days_left > 7:
        for_week = int(days_left/7)
        for_days = int(days_left%7)

elif num_of_days > 365: #400
    for_years = int(num_of_days/365) #1
    days_left = int(num_of_days%365) #35
    if days_left > 30 :
        for_months = int(days_left/30) #1
        for_days = int(days_left%30) #5
    elif days_left < 30:
        for_days = days_left
else:
    for_years = 1





print("total number of days are : ", num_of_days)
print("total number of years: " + str(for_years) + " and total number of months: " + str(for_months) + " and total weeks: " + str(for_week) + " and days: " + str(for_days))