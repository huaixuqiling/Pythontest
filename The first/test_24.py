# #读文件
# f=open("./resources/操作文件.txt","r",encoding="utf-8")

# content=f.read()
# print(content)

# content=f.readlines()
# print(content)
# for line in content:
#     print(line)
#
# f.close()

# #写文件
# f=open("./resources/静夜思.txt","w",encoding="utf-8")
#
# f.write("静夜思，礼包\n\n")
# f.write("举头望明月\n")
# f.write("静夜\n")
# f.write("低头思故乡\n")
# f.write("静\n")
#
# f.close()

# #写文件
# f=open("./resources/静夜思.txt","w",encoding="utf-8")
# try:
#     f.write("静夜思，礼包\n\n")
#     f.write("举头望明月\n")
#     f.write("静夜\n")
#     i=i/0
#     f.write("低头思故乡\n")
#     f.write("静\n")
# finally:
#     print("关闭文件")
#     f.close()

#写文件
with open("./resources/静夜思.txt","w",encoding="utf-8") as f:
    f.write("静夜思，礼包\n\n")
    f.write("举头望明月\n")
    f.write("静awd夜\n")
    f.write("低头思故乡\n")
    f.write("静\n")
