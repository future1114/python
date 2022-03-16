# 1
print("1:\n")
r=25
area=3.1415*r*r
print(area)
print("{:.2f}".format(area))
# 2
print("2:\n")
name = input("请输入姓名：")
print("{}同学，学好python，前途无量！".format(name))
print("{}大侠，学好python，大展拳脚！".format(name[0]))
print("{}哥哥，学好python，人见人爱".format(name[1:]))
# 3
print("3:\n")
a,b = 0,1
while a<1000:
    print(a,end=',')
    a,b = b,a+b
#4
import turtle
turtle.pensize(2)
turtle.circle(10)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)
#5
print("5:\n")
from datetime import datetime
now = datetime.now()
print(now)
now.strftime("%x")
now.strftime("%x")
#6
print("6:\n")
diet=['西红柿','花椰菜','黄瓜','牛排','虾仁',]
for x in range(0,5):
    for y in range(0,5):
        if not(x==y):
            print("{}{}".format(diet[x],diet[y]))
#7
print("7:\n")
str1=input("请输入一个人的名字：")
str2=input("请输入一个国家的名字：")
print("世界这么大，{}想去{}看看".format(str1,str2))
#8
print("8:\n")
n = input("请输入整数N：")
sum = 0
for i in range(int(n)):
    sum += i+1
print("1到N求和结果：",sum)
#9
print("9\n")
for i in range(1,10):
    for j in range(1,i+1):
        print("{} * {} = {:2}".format(j,i,i * j),end = ' ')
    print(' ')
#10
print("10\n")
sum,tmp=0,1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print("运算结果：{}".format(sum))