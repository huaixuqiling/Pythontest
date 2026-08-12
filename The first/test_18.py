#导入模块
import utils.utils_test1

utils.utils_test1.log_separator1()
utils.utils_test1.log_separator2()

from utils import utils_test1

utils_test1.log_separator1()
utils_test1.log_separator2()
utils_test1.log_separator3()

from utils import *

utils_test1.log_separator1()
utils_test1.log_separator2()
utils_test1.log_separator3()

#导入模块中功能
from utils.utils_test1 import log_separator1,log_separator2,log_separator3

log_separator1()
log_separator2()
log_separator3()