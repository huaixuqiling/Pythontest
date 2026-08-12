#面向对象编程
#类与对象
class car:
    pass
#创建对象
c1=car()
c1.color="red"
c1.brand="BMW"
c1.price=500000

print(c1)
print(c1.color)
print(c1.__dict__)

class Car:
    def __init__(self, color, model, price):
        self.color = color
        self.model = model
        self.price = price

c1=Car("red","BMW",552540)
print(c1.color)
print(c1.__dict__)

#实例方法
class Car:
    def __init__(self, color, model, price):
        self.color = color
        self.model = model
        self.price = price
    def running(self):
        print(f"{self.color} {self.model} 成功行驶")
    def total_price(self,discount,rate):
        """
        计算汽车总价
        :param discount: 折扣
        :param rste: 税率
        :return: 总价
        """
        total_cost=self.price*discount+rate*self.price
        return total_cost
# 魔法方法
    def __str__(self):
        return f"{self.color} {self.model} {self.price}"
    def __eq__(self,other):
        return self.price == other.price and self.color == other.color and self.model == other.model
    def __lt__(self,other):
        return self.price < other.price

c1 = Car("red","BMW",100000)

print(f"汽车总费用为{c1.total_price(discount=1,rate=0.02)}")
c1.running()

c2 = Car("red","BMW",1000000)
print(c2)

print(c1==c2)
print(c1<c2)

#案例
class Student:
    def __init__(self, name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english

    def __str__(self):
        return f"姓名：{self.name}语文：{self.chinese}数学：{self.math}英语：{self.english}总分：{self.chinese+self.math+self.english}"
    #修改学生成绩
    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese= chinese
        if math is not None:
            self.math= math
        if english is not None:
            self.english= english

class EduManagement:
    system_verson="1.1.0"
    system_name="教务管理系统"

    def __init__(self):
        self.student_list=[]

    def addStudent(self,student):
        name = input("请输入学生姓名：")
        for stu in self.student_list:
            if stu.name==name:
                print("该学生已经存在添加失败")
                return
        chinese = int(input("请输入语文成绩："))

        math = int(input("请输入数学成绩："))
        english = int(input("请输入英语成绩："))

        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("学生添加成功")
        else:
            print("成绩有误")

    def updateStudent(self):
        name= input(" 请输入学生姓名：")
        for stu in self.student_list:
            if stu.name==name:
                print(f"当前成绩{stu}")
                chinese =int(input("请输入修改后的语文成绩："))
                math = int(input("请输入修改后的数学成绩："))
                english = int(input("请输入修改后的英语成绩："))
                if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
                    stu.update_score(chinese,math,english)
                    print("修改成功")
                    return
                else:
                    print("成绩有误")
        print("未找到，修改失败")
    def deleteStudent(self):
        name = input(" 请输入删除的学生姓名：")
        for stu in self.student_list:
            if stu.name==name:
                self.student_list.remove(stu)
                print("删除成功")
                return
        print("未找到，删除失败")
    def findStudent(self):
        name = input(" 请输入查询的学生姓名：")
        for stu in self.student_list:
            if stu.name==name:
                print(f"学生信息：{stu}")
                return
        print("未找到，查询失败")
    def listStudent(self):
        for stu in self.student_list:
            print(stu)


#运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_verson}")

        while True:
            print()
            print("####################################################################################")
            print("1.添加学生      2.修改学生      3.删除学生      4.查询学生      5.查询所有学生      6.退出系统")
            print("####################################################################################")

            choice = input("请输入您想要进行的行动：")
            match choice:
                case "1":
                    self.addStudent()
                case "2":
                    self.updateStudent()
                case "3":
                    self.deleteStudent()
                case "4":
                    self.findStudent()
                case "5":
                    self.listStudent()
                case "6":
                    print("已退出系统")
                    break
                case _:
                    print("输入内容有误：")