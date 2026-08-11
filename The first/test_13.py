#字典dict
dict1={1:"one",2:"two",3:"three",1:"wadwd"}
print(dict1)
print(type(dict1))

#key必须是不可变的，list可变
dict2={1:"one",(20,20):"two", 3:"three"}
print(dict2)

print(dict1[1])
dict1[1]="one"
print(dict1)

#方法
dict1={1:"one",2:"two",3:"three"}

dict1[1]="one"
print(dict1)

dict1[1]="wad"
print(dict1)

print(dict1[1])
print(dict1.get(1))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

english= dict1.pop(1)
print(english)
print(dict1)

del dict1[2]
print(dict1)

#遍历
for k in dict1.keys():
    print(f"{k}:{dict1[k]}")

for item in dict1.items():
    print(f"{item[0]}:{item[1]}")

#案例 购物车管理系统
print("欢迎使用购物车管理系统")
print("\t")
print("######### 购物车系统 #########")
print("#       1.添加购物车         #")
print("#       2.修改购物车         #")
print("#       3.删除购物车         #")
print("#       4.查看购物车         #")
print("#       5.退出购物车         #")
print("############################")
dict_buy={}
while True:
    get=input("请选择您要执行的操作（1~5）：")
    match get:
        case "1":
            print("您正在使用商品添加功能")
            stname=input("请输入商品名称：")
            stprice=input("请输入商品价格：")
            stnum=input("请输入商品数量：")
            dict_buy[stname]=stprice,stnum
        case "2":
            print("您正在使用商品修改功能")
            stname = input("请输入要修改的商品名称：")
            stprice = input("请输入要修改商品价格：")
            stnum = input("请输入要修改商品数量：")
            dict_buy[stname] = stprice, stnum
        case "3":
            print("您正在使用商品删除功能")
            stname = input("请输入要删除的商品名称：")
            del dict_buy[stname]
        case "4":
            print("您正在使用商品查询功能")
            stname = input("请输入要查询的商品名称：")
            print(f"{dict_buy[stname]}")
        case "5":
            print("感谢使用本购物车系统")
            break
        case _:
            print("输入错误，请进行重试")



#综合练习  教务管理系统
print("欢迎使用教务管理系统")
print("\t")
print("######### 教务管理系统 #########")
print("#        1.添加学生信息        #")
print("#        2.修改学生信息        #")
print("#        3.删除学生信息        #")
print("#        4.查询学生信息        #")
print("#        5.列出所有学生        #")
print("#        6.统计班级成绩        #")
print("#         7.退出系统          #")
print("#############################")
students={}
while True:
    do=input("请输入您想要进行的操作（1~7）：")
    match do:
        case "1":
            stdname=input("请输入学生的姓名：")
            if(stdname not in students):
                stdchinese=float(input("请输入学生的语文成绩："))
                stdmath=float(input("请输入学生的数学成绩："))
                stdenglish=float(input("请输入学生的英语成绩："))
                students[stdname]=(stdchinese,stdmath,stdenglish)
            else:
                print("该学生已被成功录入，请勿进行重复操作")
        case "2":
            stdname = input("请输入要修改的学生的姓名：")
            if (stdname  in students):
                stdchinese = float(input("请输入学生的最新语文成绩："))
                stdmath = float(input("请输入学生的最新数学成绩："))
                stdenglish = float(input("请输入学生的最新英语成绩："))
                students[stdname] = (stdchinese, stdmath, stdenglish)
            else:
                print("该学生还未录入成绩，请先进行成绩录入")
        case "3":
            stdname = input("请输入需要删除的学生的姓名：")
            if (stdname in students):
                del students[stdname]
            else:
                print("该学生还未录入系统，请先进行录入")
        case "4":
            stdname = input("请输入需要查询的学生的姓名：")
            if (stdname in students):
                print(f"{stdname}的语文成绩为{stdchinese}，数学成绩为{stdmath}，英语成绩为{stdenglish}")
            else:
                print("该学生还未录入系统，请先进行录入")
        case "5":
            print("以下为所有学生的信息：")
            for name,score in students:
                print(f"学生姓名:{name},语文成绩{students[score][0]},数学成绩{students[score][1]},英语成绩{students[score][2]}")
        case "6":
            for n,c,m,y in students:
                print(f"班级语文成绩最高分为:{max(c)},姓名为{n}")
                print(f"班级数学成绩最高分为:{max(m)},姓名为{n}")
                print(f"班级英语成绩最高分为:{max(y)},姓名为{n}")
                print(f"班级语文成绩最低分为:{min(c)},姓名为{n}")
                print(f"班级数学成绩最低分为:{min(m)},姓名为{n}")
                print(f"班级英语成绩最低分为:{min(y)},姓名为{n}")
                print(f"班级语文成绩平均分为:{sum(c)/len(c)}")
                print(f"班级数学成绩平均分为:{sum(m)/len(m)}")
                print(f"班级英语成绩平均分为:{sum(y)/len(y)}")

        case "7":
            print("感谢对本系统的使用")
            break
        case _:
            print("输入内容有无，请重新输入")