#常见数据类型
print("Hello Python")
print(type("Hello Python"))

print(type(10))
print(type(3.14))
print(type(True))
print(type(False))
print(type(None))

num=-100.0
print(num)
print(type(num))

#isinstance判定数据类型
num=-100.0
print(num)
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,bool))

#字符串
#字符串的三种方式
s1="Hello"
s2='Python'
s3=""""
Hello:  #引号内无法注释
  这是一个三引号输出
  有什么关系
"""  #引号内无法注释

print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))

#定义字符串
#转义字符 \' \" \n \t
msg='It\'s very beautiful'
print(msg)

msg2="It's very beautiful"
print(msg2)

print("这是一个需要换行\n的句子")

print("这是一个需要缩进\t的句子")

print("这是一个需要换行缩进\n\t的句子")
print("这是一个需要缩进换行\t\n的句子")

#字符串拼接
s1="人生苦短" "我用Python"",OK"
print(s1)

msg1="人生苦短"
msg2="我用Python"
print("龟数说："+msg1+","+msg2)

#拼接练习
name="小米"
age=20
study="软件工程"
love="Python"

print("\"大家好,我叫" + name + ",今年" + str(age)+ "岁,学习的专业是" + study + ",爱好是" + love + "\"")

#字符串格式化
s1="小米"
s2="Python"

print("现在要进行字符串输出：%s,%s" %(s1,s2))

#用%s进行占位
name="小米"
age=20
study="软件工程"
love="Python"

print("\"大家好,我叫%s,今年%s岁,学习的专业是%s,爱好是%s\"" %(name,age,study,love))

#用f进行快速格式化
name="小米"
age=20
study="软件工程"
love="Python"

print(f"\"大家好,我叫{name},今年{age}岁,学习的专业是{study},爱好是{love}\"")