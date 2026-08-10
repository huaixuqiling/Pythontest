#模式匹配
day=input("请输入今天星期几：")

match day:
    case "1":
        print("今天星期一")
    case "2":
        print("今天星期二")
    case "3":
        print("今天星期三")
    case "4":
        print("今天星期四")
    case "5":
        print("今天星期五")
    case "6"|"7":
        print("今天休息日")
    case _:
        print("输入有误")


#案例 实现计算器
a=int(input("请输入第一个数字："))
b=int(input("请输入第二个数字："))
x=input("请输入运算符号：")

match x:
    case "+":
        print(f"输出结果为{a+b}")
    case "-":
        print(f"输出结果为{a-b}")
    case "*":
        print(f"输出结果为{a*b}")
    case "/" if b!=0:
        print(f"输出结果为{a/b}")
    case _:
        print("输入有误")

#练习，简易游戏系统制作
print("欢迎进入游戏，接下来您可以操作角色行动")
while True:
    catch=input("请进行角色的操作：")
    if catch not in ("退出","esc","ESC"):
        match catch:
            case "上"|"w"|"W":
                print("角色向上走了一步")
            case "下"|"s"|"S":
                print("角色向下走了一步")
            case "左" | "a" | "A":
                print("角色向左走了一步")
            case "右" | "d" | "D":
                print("角色向右走了一步")
            case " " | "跳":
                print("角色跳了一下")
            case "攻击" | "j" | "J":
                print("角色进行了一次攻击")
            case _:
                print("输入有误")
    else:
        print("结束游戏")
        break

#案例
i=0
while i<6:
    print("人生苦短，我学PYTHON")
    i=i+1
else:
    print("循环结束")

#案例2 计算1-100所有偶数相加
i=1
n=0
while i<=100:
    if i%2==0:
        n=n+i
    i=i+1
else:
    print(f"100以内所有偶数相加之和为{n}")
