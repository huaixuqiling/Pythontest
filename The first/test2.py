#字面量写法
print(100)          #整数
print(3.14)        #小数
print(True)        #布尔
print(False)        #BOOL
print("hello world")    #字符串
print(None)             #空值


#布尔本质也是整数类型
print(True+1)
print(False-1)


#变量  Py是一种动态语言 一个变量可以存储不同类型的数据
num=114.1
print(num)

num=115
print(num)

num=num+1
print(num)

num="OK"
print(num)

#案例  一次定义多个变量
base=20.7  #基础播放
incr=50  #每月新增
print("未来第一个月播放量：",base+incr)
print("未来第二个月播放量：",base+incr*2)

#案例 变量交换
a=10
b=20
c=a
a=b
b=c
print(a,b)

#练习 三量互换
a=100
b=200
c=300

d=c
c=a
a=b
b=d

print(a,b,c)
