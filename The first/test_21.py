# #练习 员工薪资管理系统
# class Man:
#     def __init__(self,name,base_salary,bonus,attendance):
#         self.name=name
#         self.base_salary=base_salary
#         self.bonus=bonus
#         self.attendance=attendance
#
#     def __str__(self):
#         return f"员工姓名：{self.name}员工基础薪资：{self.base_salary} 员工奖金：{self.bonus} 员工出勤：{self.attendance}"
#
#     def change(self,name,base_salary,bonus,attendance):
#         if name is not None:
#             self.name=name
#         if base_salary is not None:
#             self.base_salary=base_salary
#         if bonus is not None:
#             self.bonus=bonus
#         if attendance is not None:
#             self.attendance=attendance
#
# class SalarySystem:
#     def __init__(self):
#         self.Man_list=[]
#
#     def addman(self):
#         name=input("请输入员工姓名：")
#         for i in self.Man_list:
#             if i.name==name:
#                 print("该员工已存在")
#                 return
#         base_salary=input("请输入员工基础薪资：")
#         bonus=input("请输入员工奖金：")
#         attendance=input("请输入员工出勤：")
#         self.Man_list.append(Man(name,base_salary,bonus,attendance))
#         print("信息添加成功：")
#
#     def changeman(self):
#         name=input("请输入员工姓名：")
#         for i in self.Man_list:
#             if i.name==name:
#                 base_salary = input("请输入员工基础薪资：")
#                 bonus = input("请输入员工奖金：")
#                 attendance = input("请输入员工出勤：")
#                 i.change(name,base_salary,bonus,attendance)
#                 return
#         print("员工尚未被录入，请进行重试：")
#
#     def delMan(self):
#         name=input("请输入员工姓名：")
#         for i in self.Man_list:
#             if i.name==name:
#                 self.Man_list.remove(i)
#                 print("信息删除成功：")
#                 return
#         print("员工尚未被录入，请进行重试：")
#
#     def findMan(self):
#         name=input("请输入员工姓名：")
#         for i in self.Man_list:
#             if i.name==name:
#                 print(i)
#                 return
#         print("员工尚未被录入，请进行重试：")
#
#     def showMan(self):
#         for i in self.Man_list:
#             print(i)
#
#     def run(self):
#         system_verson="1.0.0"
#         print(f"欢迎使用员工薪资管理系统{system_verson} ")
#         print("##########################################################################")
#         print("1.添加员工    2.修改员工    3.删除员工    4.查询员工    5.查看所有员工    6.退出系统")
#         print("##########################################################################")
#         print("请选择您要执行的操作（1~6）：")
#         try:
#             while True:
#                 choice=input("请输入您想要进行的操作：")
#                 if choice=="1":
#                     self.addman()
#                 elif choice=="2":
#                     self.changeman()
#                 elif choice=="3":
#                     self.delMan()
#                 elif choice=="4":
#                     self.findMan()
#                 elif choice=="5":
#                     self.showMan()
#                 elif choice=="6":
#                     print("退出系统")
#                     break
#                 else:
#                     print("输入错误，请重新输入")
#         except Exception as e:
#             print("系统出现错误，请联系作者，错误内容为：",e)
#
# if __name__ == "__main__":
#     i=SalarySystem().run()
#     print(i)
from streamlit import status


#练习
class Room:
    def __init__(self,room_id,room_type,price,status):
        self.room_id=room_id
        self.room_type=room_type
        self.price=price
        self.status=status

    def __str__(self):
        return f"房间ID：{self.room_id} 房型：{self.room_type} 价格：{self.price} 状态：{self.status}"

    def addRoom(self,room_id,room_type,price,status):
        if room_id is not None:
            self.room_id=room_id
        if room_type is not None:
            self.room_type=room_type
        if price is not None:
            self.price=price
        if status is not None:
            self.status=status

    def changeRoom(self,room_id,room_type,price,status):
        if room_id is not None:
            self.room_id=room_id
        if room_type is not None:
            self.room_type=room_type
        if price is not None:
            self.price=price
        if status is not None:
            self.status=status

class Hotel:
    def __init__(self):
        self.Room_list=[Room(101,"单人间",500,"空闲"),
                        Room(102,"双人间",600,"空闲"),
                        Room(103,"三人间",700,"空闲")]

    def addroom(self):
        room_id=input("请输入房间ID：")
        for i in self.Room_list:
            if i.room_id==room_id:
                print("该房间已存在")
                return
        room_type=input("请输入房间类型：")
        price=input("请输入房间价格：")
        status=input("请输入房间状态：")
        self.Room_list.append(Room(room_id,room_type,price,status))
        print("房间添加成功：")

    def changeroom(self):
        room_id=input("请输入房间ID：")
        for i in self.Room_list:
            if i.room_id==room_id:
                room_type = input("请输入房间类型：")
                price = input("请输入房间价格：")
                status = input("请输入房间状态：")
                i.changeRoom(room_id,room_type,price,status)
                return
        print("房间尚未被录入，请进行重试：")

    def letinroom(self):
        room_id = input("请输入房间ID：")
        for i in self.Room_list:
            if i.room_id == room_id and i.status not in ["已入住","预定"]:
                i.status="已入住"
        print("房间已入住或被预定，请勿重复操作")

    def outinroom(self):
        room_id = input("请输入房间ID：")
        for i in self.Room_list:
            if i.room_id == room_id and i.status not in ["空闲","预定"]:
                i.status = "空闲"
        print("房间已空闲或被预定，请勿重复操作")

    def wantinroom(self):
        room_id = input("请输入房间ID：")
        for i in self.Room_list:
            if i.room_id == room_id and i.status not in ["已入住"]:
                i.status = "预定"
        print("房间已空闲，请勿重复操作")

    def delroom(self):
        room_id = input("请输入房间ID：")
        for i in self.Room_list:
            if i.room_id == room_id:
                self.Room_list.remove(i)

    def lookallroom(self):
        for i in self.Room_list:
            print(i)

    def looknoroom(self):
        for i in self.Room_list:
            if i.status== "空闲":
                print(i)

    def run(self):
        message_version="1.0.0"

        print(f"欢迎使用如家酒店管理系统,目前版本为{message_version}")
        print("#####################################################################")
        print("1.添加房间    2.修改房间    3.入住房间    4.退房    5.预定房间    6.查看所有房间    7.查看空闲房间    8.退出系统")
        print("#####################################################################")
        try:
            while True:
                do=input("请输入您想要进行的操作(1~8):")
                match do:
                    case "1":
                        self.addroom()
                    case "2":
                        self.changeroom()
                    case "3":
                        self.letinroom()
                    case "4":
                        self.outinroom()
                    case "5":
                        self.wantinroom()
                    case "6":
                        self.lookallroom()
                    case "7":
                        self.looknoroom()
                    case "8":
                        print("退出系统")
                        break
                    case _:
                        print("输入错误，请重新输入")
        except Exception as e:
            print("系统出现错误，请联系作者，错误内容为：",e)


if __name__=="__main__":
    Hotel().run()
