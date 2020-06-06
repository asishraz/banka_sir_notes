runs_per_ball = [3,2,4,4,6,1,1,2,4,2,6]


a = 0
b = 0
striker_pos = True

for i in runs_per_ball:
    if striker_pos:
        a = a + i
        if i %2 != 0:
            striker_pos = False
            


    else:
        b = b + i
        if i%2 != 0:
            striker_pos = True


print(b)




''''




