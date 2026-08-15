#算数运算符
print("10+3=",10+3)
print("10-3=",10-3)
print("10*3=",10*3)
print("10/3=",10/3)
print("10//3=",10//3)
print("10%3=",10%3)
print("10**3=",10**3)

#算数运算符的优先级  ** —— * / // % —— + -
print("0.1+10/4**2=",0.1+10/4**2)

#案例 输出 x+y x-y
x=input("请输入x的数值")
y=input("请输入y的数值")

print(f"x+y的结果为{int(x)+int(y)}")
print(f"x-y的结果为{int(x)-int(y)}")


x=float(input("请输入x的数值"))
y=float(input("请输入y的数值"))

#0.099999999998      精度损失 二进制进行计算可能损失精度
print(f"x+y的结果为{x+y}")
print(f"x-y的结果为{x-y}")

#练习1 计算输入三个数的平均数
num1=float(input("请输入第一个数："))
num2=float(input("请输入第二个数："))
num3=float(input("请输入第三个数："))

print(f"三个数的平均数为{(num1+num2+num3)/3}")

#练习2 梯形面积计算
on=float(input("请输入梯形的上底："))
down=float(input("请输入梯形的下底："))
high=float(input("请输入梯形的高："))

print(f"梯形的面积为{(on+down)*high/2}")

#练习3 计算圆的周长和面积
r=float(input("请输入圆的半径："))

print(f"圆的周长为{2*3.14*r}")
print(f"圆的面积为{3.14*r**2}")

#练习4 身体BMI的计算
weight=float(input("请输入您的体重："))
height=float(input("请输入您的身高："))

print(f"您身体指数BMI为：{weight/height**2}")

#赋值运算符
num=25
print("nun=",num)
num+=35
print("num+=35后，nun=",num)
num-=5
print("num-=5后，nun=",num)
num*=10
print("nu*+=10后，nun=",num)
num/=5
print("num/=5后，nun=",num)
num//=10
print("num//=10后，nun=",num)
num%=3
print("num%=3后，nun=",num)
num**=3
print("num**=3后，nun=",num)

#比较运算符
print("100==100吗？",100==100)
print('"100"=="100"？',"100"=="100")
print("100!=100吗？",100!=100)

print("100<100吗？",100<100)
print("100<=100吗？",100<=100)

print("100>100吗？",100>100)
print("100>=100吗？",100>=100)

#逻辑运算符 and or not
#案例1
num=int(input("请输入一个整数："))

print(f"{num}在10-20之间",num>=10 and num<=20)
print(f"{num}在10-20之间", 10 <= num <= 20)

#案例2
num=int(input("请输入一个整数："))

print(f"{num}不在10-20之间",num<10 or num>20)
