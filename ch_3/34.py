#wap to enter 100 numbers and print the frequency of following class interval in seperate columns

#class interval  frequency 
#0-10 
#11-20
#21-30
#31-40
#41-50
#above 50

freq_10 = 0
freq_20 = 0
freq_30 = 0
freq_40 = 0
freq_50 = 0
freq_60 = 0

user_input = [int(input("enter the number: ")) for x in range(10)]

for i in user_input:
    if i <= 10 and i > 0:
        freq_10 += 1
    elif i >= 11 and i <=20:
        freq_20 += 1
    elif i >= 21 and i <= 30:
        freq_30 += 1
    elif i >= 31 and i <= 40:
        freq_40 += 1
    elif i >= 41 and i <= 50:
        freq_50 += 1
    elif i > 50:
        freq_60 += 1
print("class interval                     total frequency")
print()
print("the range 1-10 having frequency:    " + str(freq_10))
print("the range 11-20 having frequency:    " + str(freq_20))
print("the range 21-30 having frequency:    " + str(freq_30))
print("the range 31-40 having frequency:    " + str(freq_40))
print("the range 41-50 having frequency:    " + str(freq_50))
print("the range 50+ having frequency:    " + str(freq_60))