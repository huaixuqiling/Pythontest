#函数
def main11():
    print("这是一个函数")
    return 0
main11()

#计算圆的面积
def cercle_area(r):
    area=3.14*r*r
    return area
c_area=cercle_area(3)
print(c_area)

#长方形面积计算
def cfx(a,b):
    """
    本函数旨在用长方形的长和宽计算长方形的面积
    :param a: 长方形的长
    :param b: 长方形的宽
    :return: 长方形的面积
    """
    area=a*b
    return area
help(cfx)

r_area=cfx(3,4)
print(r_area)

#嵌套调用 栈 先进后出
def functiona():
    print("a_____before")
    functionb()
    print("a_____end")
def functionb():
    print("b_____before")
    functionc()
    print("b____end")
def functionc():
    print("c_____ok")

functiona()


#案例1 根据传入三机型底和高计算三角形面积
def triangle_area(l,h):
    """
    本函数旨在计算三角形面积
    :param l: 三角形底长
    :param h: 三角形高长
    :return: 三角形面积
    """
    area=l*h*0.5
    return area
y_area=triangle_area(5,5)
print(y_area)

#案例2 计算字符中元音字母的个数

def Vowel_letters(string):
    vowels=("a","e","i","o","u")
    n=0
    for i in string:
        if i in vowels:
            n+=1
    return n
y_vowel_letters=Vowel_letters("y")
print(y_vowel_letters)

#案例3 计算班级高考成绩的最高分，最低分，平均分（保留一位小数），并返回
def score0(list):
    maxscore=max(list)
    minscore=min(list)
    sumscore=sum(list)/len(list)
    return maxscore,minscore,sumscore
class_score=score0([12,564,4,86,786,74,86,4,6,4,6,4,6,4,6,46,8,4,684,86])
print(class_score)

#练习1
def score(s):
    if s>=90:
        return "A"
    elif s>=75:
        return "B"
    elif s>=60:
        return "C"
    else:
        return "D"

yscore=float(input("请输入您的分数："))
print(score(yscore))

#练习2
def Palindrome(str):
    return str==str[::-1]
pal=input("请输入您的字符串：")
print(Palindrome(pal))

#练习3
def time(s):
    new_s=s%60
    min=s//60
    new_min=min%60
    hour=min//60
    return new_s,new_min,hour

se=int(input("请输入秒数"))
print(time(se))

#练习5
def Triangle(a,b,c):
    if a+b<c or b+c<a or c+a<b:
        return ("这三个边无法组成三角形，请重新输入")
    elif a==b==c:
        return ("三角形为等边三角形")
    elif a==b or b==c or c==a:
        return ("三角形为等腰三角形")
    else:
        return ("三角形为普通三角形")
print(Triangle(10,5,5))


#练习
def is_prime(n):
    if n%2==0 and n%3==0 and n%5==0 and n%7==0 and n%11==0and n%13==0and n%17==0 and n%19==0:
        return True
    else:
        return False

def taxi_fee(distance, wait_time):
    money=10
    if distance>=3:
        money+=(distance-3)*2
    if wait_time>=0:
        if wait_time%5!=0:
            money+=wait_time//5+1
        else:
            money+=wait_time//5
