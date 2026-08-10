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