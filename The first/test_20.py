# #购物车管理系统
#
# class Goods:
#     def __init__(self,name,num,count):
#         self.name=name
#         self.num=num
#         self.count=count
#
#     def __str__(self):
#         print(f"商品：{self.name}数量：{self.num}价格：{self.count}}}")
#
#     def updateGoods(self,name,num,count):
#         if name is not None:
#             self.name=name
#         if num is not None:
#             self.num=num
#         if count is not None:
#             self.count=count
#
# class ShoppingCart:
#     def __init__(self):
#         self.goods_list=[]
#
#     def addGoods(self,goods):
#         goods_name=input("请输入要添加的物品名称：")
#         for goods in self.goods_list:
#             if goods.name==goods_name:
#                 print("该商品已经在库中，请重新输入")
#                 return
#         goods_num=input("请输入商品的数量：")
#         goods_count=input("请输入商品的价格：")
#
#         goods=Goods(goods_name,goods_num,goods_count)
#         self.goods_list.append(goods)
#         print("添加成功")
#
#     def changeGoods(self,goods):
#         goods_name = input("请输入要修改的物品名称：")
#         for goods in self.goods_list:
#             if goods.name != goods_name:
#                 print("该商品还未入库，请重新输入")
#                 return
#         goods_num = input("请输入商品的数量：")
#         goods_count = input("请输入商品的价格：")
#         goods.updatedGoods(goods_name,goods_num,goods_count)
#
#     def delGoods(self,goods):
#         goods_name = input("请输入要删除的物品名称：")
#         for goods in self.goods_list:
#             if goods.name != goods_name:
#                 print("该商品还未入库，请重新输入")
#                 return
#         self.goods_list.remove(goods_name)
#
#     def showGoods(self):
#         goods_name = input("请输入要查询的物品名称：")
#         for goods in self.goods_list:
#             if goods.name == goods_name:
#                 print(f"{goods}")
#
#
#     def runShoppingCart(self):
#         print("")
#
#
#
# #练习2 图书管理
# class Book:
#     def __init__ (self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#
#     def __str__(self):
#         return f"{self.title} {self.author} {self.price}"
#
#     def update_price(self,title,author,price):
#         if title is not None:
#             self.title=title
#         if author is not None:
#             self.author=author
#         if price is not None:
#             self.price=price
#
# class Library:
#     def __init__(self):
#         self.books_list=[]
#
#     def add_book(self):
#         book_name=input("请输入书的名字：")
#         for i in self.books_list:
#             if i.title == book_name:
#                 print("该书已被添加，请重新输入：")
#                 return
#         book_author=input("请输入书的作者：")
#         book_price=input("请输入书的价格：")
#         self.books_list.append(Book(book_name,book_author,book_price))
#
#     def look_books(self):
#         book_name = input("请输入借阅书的名字：")
#         for i in self.books_list:
#             if i.title == book_name:
#                 self.books_list.remove(i)
#


#异常
try:
    print("__________________")
    # print(myname)
    # print(1/0)
    print("ABC"[10])
    print("_________________")
except NameError as e:
    print("Name Error")
    print("代码出错了",e)
except ZeroDivisionError as e:
    print("代码出错了",e)
except Exception as e:
    print("代码出错了", e)
finally:
    print("结束")