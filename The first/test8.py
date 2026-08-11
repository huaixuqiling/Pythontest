#for循环
msg="Hello_World"

for i in msg:
    print(i)
else:
    print("遍历结束")

msg=input("请输入要遍历的元素")

for s in msg:
    print(f"元素：{s}")
else:
    print("遍历结束！")

#案例1 计算1-100的基数之和
msg=range(1,101,2)
n=0
for i in msg:
    n=n+i
else:
    print(f"100以内基数之和为{n}")

#案例2 计算100-500的3倍数字之和
msg=range(100,501)
n=0
for i in msg:
    if i%3==0:
        n=n+i
else:
    print(f"100-500的3倍数字之和为{n}")

#嵌套循环
m=int(input("请输入长方形的长度"))
n=int(input("请输入长方形的宽度"))

for j in range(n):
    for i in range(m):
        print("*", end="  ")
    print()
else:
    print("循环结束")

#案例 99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i} x {j} =" f"{i*j}",end="\t")
    print("")

#练习1 输入等腰三角形

n=int(input("输入直角边的边长"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")

#练习2 根据输入的数字输出数字金字塔

n=int(input("请输入您的数字："))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")

#练习3 打印国际象棋棋盘

n = int(input("请输入棋盘行数："))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()

#案例
while True:
    uesrname = input("请输入您的用户名:")
    password = input("请输入您的密码:")
    if uesrname=="admin" and password=="666888":
        print("登陆成功，进入B站首页")
        break
    elif uesrname=="zahngsan" and password=="123456":
        print("登陆成功，进入B站首页")
        break
    elif uesrname=="taoge" and password=="888666":
        print("登陆成功，进入B站首页")
        break
    elif uesrname=="" or password=="":
        print("同户名和密码不能为空")
    else:
        print("用户名或密码错误，请重新输入:")

#练习

for i in range(5):
    uesrname = input("请输入您的用户名:")
    password = input("请输入您的密码:")
    if uesrname=="" or password=="":
        print("同户名和密码不能为空")
        continue
    if uesrname=="admin" and password=="666888":
        print("登陆成功，进入B站首页")
        break
    elif uesrname=="zahngsan" and password=="123456":
        print("登陆成功，进入B站首页")
        break
    elif uesrname=="taoge" and password=="888666":
        print("登陆成功，进入B站首页")
        break
    else:
        print("用户名或密码错误，请重新输入:")

#案例2 猜数字

import random
random_number=random.randint(1,100)
while True:
    num=int(input("请输入您的数字:"))
    if num==random_number:
        print("猜对了！")
        break
    elif num>random_number:
        print("输入的数字大了")
    elif num<random_number:
        print("输入的数字小了")
    else:
        print("输入错误，请重新输入")

#练习1
n=0
for i in range(1,1001):
    if i%5==0:
        n=n+i
print(f"1000以内所有5倍数字累加起来之和为{n}")

#练习2 统计字符串“akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd”中有多少个a和k

msg="akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
numa=0
numk=0
for i in msg:
    if i=="a":
        numa+=1
    elif i=="k":
        numk+=1
print(f"字符串中a的个数为{numa}，k的个数为{numk}")
