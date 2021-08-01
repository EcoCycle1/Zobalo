import time

x =  time.localtime()
xs = int(time.strftime("%S", x))
xm = int(time.strftime("%M", x))
xh = int(time.strftime("%H", x))
x = 60*xm+xs+xh*3600
print(x)
time.sleep(5)
y =  time.localtime()
xs = int(time.strftime("%S", y))
xm = int(time.strftime("%M", y))
xh = int(time.strftime("%H", y))
y = 60*xm+xs+xh*3600
z=y-x
print(z)
print(y)