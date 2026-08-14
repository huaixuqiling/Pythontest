#写入JSON 数据
import json

user={
    "name":"启灵",
    "age":18,
    "gender":"男"
}
with open("./resources/uesr.txt","w",encoding="utf-8") as f:
    json.dump(user,f,ensure_ascii=False)


with open("./resources/uesr.txt","r",encoding="utf-8") as f:
    user=json.load(f)
    print(user)