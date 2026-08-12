#类型注解
a: int=20
b: float=2.5
c: str="Python"
d: bool=True
e: None=None

f: list[str]=["A","C","B","D"]
g: set[str]={"A","B","C","D","E","F","G"}
h: dict[str,int]={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6}
i: tuple[str,int,int]=("一等bin",1,5)

f.append("21")

#类型推断________Python 会根据类型进行自动推断

#函数类型注解
def circle_area(r: float)->tuple[float,float]:
    return round(3.14*r**2,1),round(2*3.14*r,1)

al=circle_area(5)
print(al)