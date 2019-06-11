from datetime import *

today = datetime.now()                  # 打印当前的时间
print(today)
print(datetime.date(today))             # 根据当前时间打印日期
print(datetime.time(today))             # 根据当前时间打印时间
print(datetime.ctime(today))            # 根据当前时间获取"星期 月份 日 时:分:秒.毫秒 年"格式的时间


# 标准库之time.
import time

time.sleep(0.3)         # 设置延迟时间,经常用来设置进程暂停的时间
print(time.time())      # 可用来统计一段程序的运行时间
print(time.time())
