import sys


# 退出程序的运行
# sys.exit(20)

# 统计执行文件时的参数
list01 = sys.argv
print(list01)
# Out:
# (venv) localhost:cloudpybasis chaoliu$ python3 08.stdlib_module/02.syslibs.py 1 2 3 4 5
# ['08.stdlib_module/02.syslibs.py', '1', '2', '3', '4', '5']

# 获取文件编码
encoding = sys.getfilesystemencoding()
print(encoding)

#