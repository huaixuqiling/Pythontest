#不定长参数
def calc_data(*args):
    min_data=min(args)
    max_data=max(args)
    avg_data=sum(args)/len(args)
    return min_data,max_data,round(avg_data,1)

print(calc_data(6,48,64,6,4,87,5,4,8,48,4,8,76,6,7,87,8,4,8))
print(calc_data(6,48,64,6,4,87,5,4,8,48,4,8))

#关键字不定
def calc_data(*args,**kwargs):
    min_data=min(args)
    max_data=max(args)
    avg_data=sum(args)/len(args)

    if kwargs.get('round') is not None:
        avg_data=round(avg_data,kwargs.get('round'))\

    if kwargs.get('print') is not None:
        print(f"计算出来的最大值为{max_data}")

    return min_data,max_data,avg_data

print(calc_data(6,48,64,6,4,87,5,4,8,48,4,8,76,6,7,87,8,4,8,round=3,print=True))
print(calc_data(6,48,64,6,4,87,5,4,8,48,4,8))

#参数类型
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def power(a,b,st):
    return st(a,b)

print(power(2,3,add))

#匿名函数
out_line=lambda : print('hello world')
add=lambda a,b: a+b

out_line()
print(add(1,2))

#需求
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
data_list.sort()
print(data_list)

data_list.sort(key=lambda item:len(item),reverse=True)
print(data_list)


#案例 递归调用
def numl(num):
    if num==1:
        return 1
    else:
        return num*numl(num-1)
dv=numl(10)
print(dv)

#案例
def clac_order_cost(*args,coupon=0,score=0,express=0):
    total_price=[st[2]*st[3] for st in args]
    total_cost=sum(total_price)
    if total_cost>=5000 and coupon<=total_cost:
        total_cost=total_cost-coupon

    if total_cost >= 5000 and score//100 <= total_cost:
        total_cost = total_cost - score//100

    total_cost=total_cost+express
    return total_cost