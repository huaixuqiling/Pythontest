#函数变量作用域
num=100

def circle(r):
    pi=3.14
    area=pi*r*r
    global num
    num=4157845864
    print(num)
    return area

c_area=circle(num)
print(c_area)
print(num)

#传参方式
def reg_stu(name, age, gender, city):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}
#位置传参
reg_stu("huai",213,"男","背景")

#关键值传参
reg_stu(name="阿迪王",age=231,city="挖的哇",gender="男")

#混合传参
reg_stu("huai",213,city="挖的哇",gender="女")

#默认参数
def reg_stu(name, age, gender="男", city="北京"):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

reg_stu("huai",213)
reg_stu("huai",213,city="背景")
reg_stu("huai",213,"男")