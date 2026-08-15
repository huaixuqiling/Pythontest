#列表list
s=[51,45,9,8,894,894,66,786,66,True,"545","dawdwad"]
print(type(s))

print(s[2])
print(s[-10])

print(s)
s[2]="ABC"
print(s)

del s[2]
print(s)

for i in s:
    print(i)

#列表切片  很像range
s=[51,45,9,8,894,894,66,786,66,True,"545","dawdwad"]

print(s[0:6:1])
print(type(s[0:6:1]))

print(s[:6:1])
print(s[:6:])
print(s[:6])
print(s[6:])
print(s[6])

print(s[0:-2:1])

#列表方法

s=[1,2,3,7,4,5,6,7,8,9]

s.append(188)
print(s)

s.insert(1,188)
print(s)

s.remove(2)
print(s)

s.pop(1)
print(s)
s.pop()
print(s)

s.sort()
print(s)

s.reverse()
print(s)

#案例    sum求和 len()获取元素的个数
s=[]
for i in range(10):
    num=int(input("请输入数字:"))
    s.append(num)
s.sort()
print(s)
print(f"数组中最小的数字为{s[0]}")
print(f"数组中最大的数字为{s[9]}")
print(f"数组的平均值为{(sum(s))/10}")


#案例 列表合并
num_list1=[78,415,36,4,6,48,86,4,54,68,4,11,6]
num_list2=[78,3215,684,31,4,6,95,68,46,8]

for i in num_list2:
    num_list1.append(i)
print(num_list1)

new_list=[]
for i in num_list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)

#案例 列表合并/简化
num_list1=[78,415,36,4,6,48,86,4,54,68,4,11,6]
num_list2=[78,3215,684,31,4,6,95,68,46,8]

#解包 将列表解开成独立的元素
#组包 将多个值合并到一个容器
num_list=[*num_list1,*num_list2]
print(num_list)

#案例 列表合并/方案3
num_list1=[78,415,36,4,6,48,86,4,54,68,4,11,6]
num_list2=[78,3215,684,31,4,6,95,68,46,8]

num_list=num_list1+num_list2
print(num_list)

#案例1
n=[]
for i in range(1,21):
    n.append(i**2)
print(n)

#案例1 列表推导式 按照规则快速生成列表
n=[i**2 for i in range(1,21)]
print(n)

#案例2
num_list=[19,23,54,64,87,20,109,232,123,43,26,55,72]
new_list=[]
for i in num_list:
    if i%2==0:
        new_list.append(i**2)
print(new_list)

#案例2 列表推导式方法       要插入的值 for i in 列表 if 条件
num_list=[19,23,54,64,87,20,109,232,123,43,26,55,72]
new_list=[i**2 for i in num_list if i%2==0]
print(new_list)

#练习1
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']
new_list = list1 + list2 + list3
lista=[]
for i in new_list:
    if i not in lista:
        lista.append(i)
lista.sort()
print(lista)

#练习2
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
new_list=[i**2 for i in list1 if i%3==0 or i%5==0]
print(new_list)

#练习3
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
new_list=[i for i in list1 if i>=0]
print(new_list)

#练习 从列表 list1 中提取所有能被 4 或 7 整除的元素，计算它们的立方（i ** 3），组成一个新的列表并输出
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
new_list=[i**3 for i in list1 if i%7==0 or i%4==0]
print(new_list)
