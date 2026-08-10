#条件判断
score=700
if score>700:
    print("进入清华读书")
else:
    print("11")
print("_____________________________________")

#案例 登录账号密码
ok_account="123456"
ok_password="111"

account=input("请输入账号")
password=input("请输入密码")

if account==ok_account and password==ok_password:
    print("登陆成功")
if account != ok_account or password != ok_password:
    print("账号和密码错误")

#案例 登录账号密码   else
ok_account="123456"
ok_password="111"

account=input("请输入账号")
password=input("请输入密码")

if account==ok_account and password==ok_password:
    print("登陆成功")
else:
    print("账号和密码错误")

#练习1 判断年份

year=int(input("请输入您的年份："))

if year%100==0 and year%400==0:
    print("年份为闰年")
elif year%4==0:
    print("年份为闰年")
else:
    print("年份不是闰年")

#练习2 判断基数还是偶数
num=float(input('请输入您的数字：'))
if num%2==0:
    print("数字为偶数")
else:
    print("数字为基数")

#练习3 判断未成年
age=int(input("请输入您的年龄："))
if age>=18:
    print("成年了")
else:
    print("未成年")

#练习4 判断正负数
num=float(input("请输入您的数字："))
if num>0:
    print("数字为正数")
else:
    print("数字为负数")

#练习5 判断及格
score=float(input("请输入成绩："))
if score>=60:
    print("成绩及格")
else:
    print("成绩不及格")

#elif 判断正负零
num=float(input("请输入您的数字："))
if num>0:
    print("数字为正数")
elif num<0:
    print("数字为负数")
else:
    print("数字为零")

#案例三套账号密码
username=input("请输入用户名")
password=input("请输入密码")

if username=="root" and password=="123456":
    print("登陆成功")
elif username=="admin" and password=="123456":
    print("登陆成功")
elif username == "awdawd" and password == "123456":
    print("登陆成功")
else:
    print("登录失败")

#练习1 判断成绩
score=float(input("请输入成机"))
if score>=85:
    print("成绩为优秀")
elif score>=60 and score<85:
    print("成绩为及格")
else:
    print("成绩不及格")

#练习2 判断购物车商品价格
money=float(input("请输入商品总价格："))
if money>=500:
    print(f"商品为8折，您总共应付款{money * 0.8}元")
elif money>=300 and money < 500:
    print(f"商品为9折，您总共应付款{money * 0.9}元")
elif money >= 100 and money < 300:
    print(f"商品为95折，您总共应付款{money * 0.95}元")
else:
    print(f"商品为不打折，您总共应付款{money}元")


#案例 三角形形状判断
a=int(input("请输入三角形第一个边长度为："))
b=int(input("请输入三角形第二个边长度为："))
c=int(input("请输入三角形第三个边长度为："))

if a==b==c:
    print("该三角形为等边三角形")
elif a+b<=c or b+c<=a or a+c<=b:
    print("该三条边无法组成三角形")
elif a==b or b==c or c==a:
    print("该三角形为等腰三角形")
else:
    print("该三角形为普通三角形")

#练习 电费计算
ele=float(input("请输入本年用的电费度数："))

if ele<=2880:
    print(f"本年度电费为第一档，应付款{ele*0.4883}元")
elif 2880<=ele<=4800:
    print(f"本年度电费为第二档，应付款{(ele-2880)*0.5383+2880*0.4883}元")
else:
    print(f"本年度电费为第三档，应付款{(ele-4800)*0.7883+(4800-2880)*0.5383+2880*0.4883}元")