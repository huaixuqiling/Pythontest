#字符串 str
s="Hello_World"
print(s[4])
print(s[-4])
# 字符串无法修改值
# s[4]="X"
# print(s)

for i in s:
    print(i)

#切片
print(s[0:5:1])
print(s[0:5:])
print(s[:5:])
print(s[:5])

print(s[-1:-7:-1])
print(s[::-1])

#字符串方法 无法删除修改
s="Hello_World_Hello_Python"

a=s.find("_")
print(a)

b=s.count("_")
print(b)

c=s.upper()
print(c)

d=s.lower()
print(d)

e=s.split("_")
print(e)
print(isinstance(e,list))

#去除两边空格
f=s.strip()
print(f)

g=s.replace("_","--")
print(g)

h=s.startswith("Hello")
print(h)
i=s.endswith("_")
print(i)

#案例 邮箱格式验证
email=input("请输入您的邮箱：")
if email.count("@") == 1 and email.count(".") >= 1:
    print(f"{email}是合法的邮箱")
else:
    print(f"{email}是不合法的邮箱")

#案例 邮箱格式验证 方式2
email=input("请输入您的邮箱：")
if email.count("@") == 1 and "." in email:
    print(f"{email}是合法的邮箱")
else:
    print(f"{email}是不合法的邮箱")

#练习1
# "黄山落叶松叶落山黄"
# "上海自来水来自海上"
str1=input("请输入一段文字：")
if str1[::1] == str1[::-1]:
    print("该文字为回文")
else:
    print("该文字不是回文")

#练习2
str_list=[]
for i in range(10):
    num=input(f"请输入第{i+1}个字符串：")
    str_list.append(num.upper())
str_list.reverse()
print(str_list)

for a in str_list:
    print(a)

#练习

a=input("请输入一个字符串")

numi=a.count("i")
print(numi)
st=a.endswith("ing")
print(st)