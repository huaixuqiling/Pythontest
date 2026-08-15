#练习 记账
class total_money:
    def __init__(self,all_money:float,addmoney:float,cutmoney:float,money_type,note):
        self.all_money=all_money
        self.addmoney=addmoney
        self.cutmoney=cutmoney
        self.money_type=money_type
        self.note=note

    def __str__(self):
        return f"总金额为：{self.all_money} 收入的金额为：{self.addmoney} 支出的金额为：{self.cutmoney} 金额类型为：{self.money_type} 备注为：{self.note}"

class MoneySystem:
    def __init__(self):
        self.money_list=[]
        self.all_money=0

    def AddMoney(self):
        addmoney=float(input("请输入要添加的金额"))
        if addmoney>=0:
            money_type=input("请输入收入的类型")
            note=input("请输入收入的备注")
            self.all_money+=addmoney
            addMoney=total_money(self.all_money,addmoney,0,money_type,note)
            self.money_list.append(addMoney)
        else:
            print("请输入正确的数字")

    def CutMoney(self):
        cutmoney=float(input("请输入要支出的金额"))
        if cutmoney>=0:
            money_type=input("请输入支出的类型")
            note=input("请输入支出的备注")
            self.all_money-=cutmoney
            cutMoney=total_money(self.all_money,0,cutmoney,money_type,note)
            self.money_list.append(cutMoney)
        else:
            print("请输入正确的数字")

    def lookdo(self):
        for look in self.money_list:
            print(look)

    def looktotal(self):
        total_addmoney=0
        total_cutmoney=0
        for look in self.money_list:
            total_addmoney+=look.addmoney
            total_cutmoney+=look.cutmoney
        print(f"总收入为：{total_addmoney}")
        print(f"总支出为：{total_cutmoney}")
        print(f"当前余额为：{self.all_money}")

    def run(self):
        print("====================记账小程序====================")
        print("1. 添加收入 2. 添加支出 3. 查看记录 4. 查看统计 5. 退出")
        print("=================================================\n")
        try:
            while True:
                do = int(input("请输入您想要进行的操作1~5："))
                match do:
                    case 1:
                        self.AddMoney()
                    case 2:
                        self.CutMoney()
                    case 3:
                        self.lookdo()
                    case 4:
                        self.looktotal()
                    case 5:
                        print("正在结束小程序")
                        break
                    case _:
                        print("请输入正确的选项")
        except Exception as e:
            print(f"程序出现错误，错误为：{e}")

if __name__=="__main__":
    run1=MoneySystem()
    run1.run()