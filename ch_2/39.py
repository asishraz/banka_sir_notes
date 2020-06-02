#wap to enter two seperate time duration in hrs,minutes and seconds and put their sum
#e.g 13hr 50 min 20 sec  + 10hr 50 min 50 sec = 24hr 41 min 10 sec


first_hr = int(input("enter the time in hrs: "))
first_min = int(input("enter the time in min: "))
first_sec = int(input("enter the time in sec: "))

second_hr = int(input("enter the time in hrs: "))
second_min = int(input("enter the time in min: "))
second_sec = int(input("enter the time in sec: "))


add_sec = first_sec + second_sec
add_min = first_min + first_min
add_hr = first_hr + second_hr

if add_sec >= 60:
    add_min += 1
    add_sec = add_sec - 60
    if add_min >= 60:
        add_hr += 1
        add_min -= 60
        print("Total hrs: " +str(add_hr) + " and total minutes: " +str(add_min) + " and total seconds: " +str(add_sec))
    elif add_min < 60:
        print("Total hrs: " +str(add_hr) + " and total minutes: " +str(add_min) + " and total seconds: " +str(add_sec))

elif add_sec < 60:
    if add_min >= 60:
        add_hr += 1
        add_min -= 60
        print("Total hrs: " +str(add_hr) + " and total minutes: " +str(add_min) + " and total seconds: " +str(add_sec))
    elif add_min < 60:
        print("Total hrs: " +str(add_hr) + " and total minutes: " +str(add_min) + " and total seconds: " +str(add_sec))

    


