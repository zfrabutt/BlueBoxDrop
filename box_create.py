import subprocess

i = 0
x = 25
y = 25
model = "box"

while (i < 26):
    
    model = "box" + str(i)

    x = 25 - (2 * i)   
    i = i + 1
    subprocess.check_call(['./square_shape.sh', model, str(y), str(x)])

i = 0
x = 25
y = -25

while (i < 26):
    
    model = "boxa" + str(i)

    x = 25 - (2 * i)   
    i = i + 1
    subprocess.check_call(['./square_shape.sh', model, str(y), str(x)])

i = 0
x = 25
y = 23

while (i < 24):
    
    model = "boxb" + str(i)

    y = 23 - (2 * i)   
    i = i + 1
    subprocess.check_call(['./square_shape.sh', model, str(y), str(x)])

i = 0
x = -25
y = 23

while (i < 24):
    
    model = "boxc" + str(i)

    y = 23 - (2 * i)   
    i = i + 1
    subprocess.check_call(['./square_shape.sh', model, str(y), str(x)])

