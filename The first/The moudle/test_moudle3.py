#导入模块
import  test_moudle2

#使用模块中功能
print(test_moudle2.PI)
print(test_moudle2.NAME)

test_moudle2.log_separator1()
test_moudle2.log_separator2()
test_moudle2.log_separator3()

 #导入模块的功能
from test_moudle2 import log_separator1,log_separator2,log_separator3,PI,NAME
# from  test_moudle2 import *
# 使用模块中功能
print(PI)
print(NAME)

log_separator1()
log_separator2()
log_separator3()
