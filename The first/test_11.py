#元组

t1=(12,12,45,8,7,87,7,9,7,True,65)

t2=()
t3=tuple()
print(t1)
print(t1[-1])
print(t1[0])
print(type(t1))

print(t1[:5:1])

print(t1.count(12))
print(t1.index(12))

t0=(100,)
print(t0)
print(type(t0))

t1=(12,12,45,65)

t2=12,12,45,65

a,b,c,d=t1
print(a,b,c,d)

a,*b,d=t1
print(a,b,d)

#案例
a=10
b=20

a,b=b,a
print(a,b)

#案例2
a=100
b=200
c=300

a,b,c=c,b,a
print(a,b,c)

#案例3
students = (
    ("G001","王林",85,92,78),
    ("G002","李敏娟",92,88,95),
    ("G003","十三",78,85,82),
    ("G004","曾伟",88,79,91),
    ("G005","周敏",95,96,89),
    ("G006","王卓",76,82,77),
    ("G007","江斌",89,91,94),
    ("G008","徐立国",75,69,82),
    ("G009","许木",86,89,86),
    ("G010","通天",66,59,72)
)

for i in students:
    sum1=i[2]+i[3]+i[4]
    avg=sum1/3
    print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{sum1}\t{avg:.1f}")

#方式2 解包
for id,name,chinese,math,english in students:
    total=chinese+math+english
    avg=total/3
    print(f"{english}")

chinese_score=[s[2] for s in students]
math_score=[s[3] for s in students]
english_score=[s[4] for s in students]

print(f"语文的最低分是{min(chinese_score)},语文的最高分是{max(chinese_score)}，语文的平均分是{sum(chinese_score)/len(chinese_score)}")



for a in students:
    sum1=a[2]+a[3]+a[4]
    avg=sum1/3
    if avg>90:
        print(f"{a[0]}")
