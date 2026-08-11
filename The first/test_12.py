#集合set
s1={5,3,5,7,98,7,9,23,4,4}
print(s1)
print(type(s1))

s2=set()
print(s2)
print(type(s2))

#集合方法
s1={100,200,300,400,500,600,700}
print(s1)

s1.add(800)
print(s1)

s1.remove(400)
print(s1)

e=s1.pop()
print(e)
print(s1)

s1.clear()
print(s1)

#案例
# 选修足球学生名单
football_set = {"王林", "曹牛", "徐立国", "通天", "天运子", "韩立", "厉飞雨", "马丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "昌昌仁", "王林", "姜老道", "曹牛", "王琳", "韩立", "天运子", "李化元", "厉飞雨", "云雷"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎胆", "姜老道", "天运子", "红娘", "厉飞雨", "韩立", "曹牛"}
# 选修艺术学生名单
art_set = {"通天", "天运子", "韩立", "虎胆", "姜老道", "紫灵"}

a=french_set.intersection(art_set)
#b=basketball_set.intersection(football_set)
b=basketball_set-football_set
print(f"通识选修了法语和艺术的学生有{french_set.intersection(art_set)}")
print(f"同时选修了四门课程的学生有{a.intersection(b)}")
print(f"选修了足球但没有选修篮球的学生有{football_set.difference(basketball_set)}")

all_set=french_set|basketball_set|art_set|football_set
print(all_set)

all_list=[*football_set,*basketball_set,*art_set,*french_set]
print(all_list)

for s in all_set:
    print(f"{s}选修了{all_list.count(s)}课程")

#练习    同时选了 Python 和 Java 的学生有哪些？
#       只选了 Python 没有选 SQL 的学生有哪些？
#       三门课都选了 的学生有哪些？
#       至少选了一门课 的学生共有多少人？
python_set = {"王林", "李敏娟", "十三", "曾伟", "周敏", "王卓"}
java_set = {"王卓", "江斌", "徐立国", "许木", "通天", "李敏娟"}
sql_set = {"十三", "曾伟", "通天", "王林", "江斌", "许木"}

pj_set=python_set & java_set
p_s_set=python_set - sql_set
all_set1=python_set & java_set & sql_set
all_set=len(python_set | java_set | pj_set)

