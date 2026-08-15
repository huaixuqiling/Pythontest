#键盘上进行输入输出
name=input("请输入您的姓名:")
age=input("请输入您的年龄:")

print(f"您的姓名是{name},您的年龄是{age}")

#案例 银行取钱
total=10000

#输入密码
password=input("请输入您的密码")
print(f"密码正确，{password}")

#输入取款金额
num=input("请输入您的取款金额：")

#计算剩余金额
print(f"取款后余额为：{total-int(num)}")

#练习计算器加法
num1=input("请输入第一个数字：")
num2=input("请输入第二个数字：")

print(f"两数相加之和为：{int(num1)+int(num2)}")