import os


# 获取当前目录的绝对路径
path = os.getcwd()
print(path)

# 获取文件的绝对路径
abspath = os.path.abspath("01.oslibs.py")
print(abspath)

# 执行shell命令
if os.system("ls /User") == 0:
    os.system("yum -y install httpd")
else:
    print("Failed")



