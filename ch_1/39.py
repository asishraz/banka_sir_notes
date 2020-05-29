#wap to enter the values of u(object vision) & v(image vision) and print the value of f(focal length) using the formula:
# 1/f = (1/u) + (1/v)


u = int(input("enter the object vision: "))
v = int(input("enter the image vision: "))
f = (u*v) / (v+u)


''' (v+u)/uv = 1/f => uv/f = v+u = > f(v+u) = uv '''


print("enter the focal length: ", f)