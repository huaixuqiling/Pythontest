__all__ = ["log_separator1", "log_separator2", "log_separator3", "log_separator4"]
#常量
PI=3.1415926
NAME="阿达瓦"

#函数
def log_separator1():
    print("-" * 30)
def log_separator2():
    print("+" * 30)
def log_separator3():
    print("#" * 30)
def log_separator4():
    print("*" * 30)

print(__name__)
if __name__ == "__main__":
    log_separator1()