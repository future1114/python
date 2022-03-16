''' 
# 1.
a = input("请输入：")
print(a)
'''
''' 
# 2.
b = input("请输入：")
b=ord(b) # python 转化为ASCII
if (97<=b)and(b<=122):
    print("这是小写字符")
elif (65<=b)and(b<=90):
    print("这是大写字符")
else:
    print("error")
'''
'''
# 3.
a = eval("1")
print(a)
a = eval('"1 + 2"')
print(a)
eval('print("hello world")')
'''
'''
# 4.
import turtle
turtle.goto(100,100)
turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(0,0)
'''
'''
# 5.
import turtle
turtle.left(45)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)
img = turtle.getscreen()
img.getcanvas().postscript(file="实验二5.eps")
'''
'''
# 6.
import imp
import turtle
import PIL
turtle.circle(100)
turtle.done()
'''
'''
# 7.
for i in range(5):
    print(i)
'''
'''
a=range(5)
for i in range(5):
    print(a[i])
'''
'''
# 8.
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2 / 3)
turtle.done()
'''
'''
# z1.
a = "请输入带有符号的温度:"
TempStr = eval("input(a)")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.0f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.0f}F".format(F))
else:
    print("输入格式错误")
'''
'''
# z2.
mon = input("请输入带有符号的钱币总额: ")
if mon[-1] in ['R','r','￥']:
    C = eval(mon[0:-1]) /6
    print("转换后的钱是{:.3f}$".format(C))
elif mon[-1] in ['$','d','$']:
    F = eval(mon[0:-1]) *6
    print("转换后的钱是{:.3f}￥".format(F))
else:
    print("输入格式错误")
'''
'''
# z3.
import turtle
import random
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.pencolor(random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100)
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2 / 3)
turtle.done()
'''
'''
# z4.
import turtle
turtle.setup(650,350,200,200)
turtle.fd(120)
turtle.seth(120)
turtle.fd(120)
turtle.seth(120*2)
turtle.fd(120)
turtle.done()
'''
'''
# z5.
import turtle
turtle.setup(650,650,200,200)
turtle.fd(240)
turtle.seth(120)
turtle.fd(240)
turtle.seth(240)
turtle.fd(120)
turtle.seth(0)
turtle.fd(120)
turtle.seth(240)
turtle.fd(120)
turtle.seth(120)
turtle.fd(120)
turtle.seth(240)
turtle.fd(120)
turtle.seth(60)
turtle.fd(120)
turtle.seth(00)
turtle.done()
'''
'''
# z6.
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(20)
turtle.pendown()
turtle.fd(100)
turtle.penup()
turtle.fd(20)
turtle.pendown()
turtle.seth(90)
turtle.penup()
turtle.fd(20)
turtle.pendown()
turtle.fd(100)
turtle.penup()
turtle.fd(20)
turtle.pendown()
turtle.seth(180)
turtle.penup()
turtle.fd(20)
turtle.pendown()
turtle.fd(100)
turtle.penup()
turtle.fd(20)
turtle.pendown()
turtle.seth(270)
turtle.penup()
turtle.fd(20)
turtle.pendown()
turtle.fd(100)
turtle.penup()
turtle.fd(20)
turtle.pendown()
turtle.seth(0)
turtle.done()
'''
'''
# z7.
import turtle
turtle.setup(650,650,200,200)
turtle.seth(30)
turtle.fd(90)
turtle.seth(150)
turtle.fd(90)
turtle.seth(270)
turtle.fd(90)
turtle.seth(30)
turtle.fd(30)
turtle.seth(330)
turtle.fd(30)
turtle.seth(90)
turtle.fd(90)
turtle.seth(210)
turtle.fd(90)
turtle.seth(330)
turtle.fd(60)
turtle.seth(150)
turtle.fd(60)
turtle.seth(30)
turtle.fd(30)
turtle.done()
'''
'''
# z8.
import turtle
turtle.setup(1000,1000,200,200)
l=10
turtle.seth(90)
turtle.fd(l)
l=l+10
turtle.seth(180)
turtle.fd(l)
l=l+10
for i in range(15):
    turtle.seth(270)
    turtle.fd(l)
    l=l+10
    turtle.seth(0)
    turtle.fd(l)
    l=l+10
    turtle.seth(90)
    turtle.fd(l)
    l=l+10
    turtle.seth(180)
    turtle.fd(l)
    l=l+10
turtle.seth(270)
turtle.fd(l)
l=l+10
turtle.seth(0)
turtle.done()
'''
'''
# z9.
import turtle
import random
turtle.setup(1400,600,200,200)
turtle.penup()
turtle.fd(-650)
turtle.seth(270)
turtle.fd(100)
turtle.seth(0)
turtle.pendown()
turtle.pensize(30)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.pencolor(random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100)
    turtle.circle(100,100)
    turtle.circle(-100,100)
turtle.circle(40,80/2)
turtle.fd(50)
turtle.circle(16,180)
turtle.fd(50 * 2 / 3)
turtle.done()
'''
