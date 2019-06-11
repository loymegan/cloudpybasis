import os


# 获取当前目录的绝对路径
path = os.getcwd()
print(path)

# 获取文件的绝对路径
abspath = os.path.abspath("01.oslibs.py")
print(abspath)

# 执行shell命令
# if os.system("ls /User") == 0:
#     os.system("yum -y install httpd")
# else:
#     print("Failed")

# 文件的增删改查
# os.mkdir("/Users/chaoliu/Documents/osmkdir", 0o777)
# os.rmdir("/Users/chaoliu/Documents/osmkdir")
os.chdir("/Users/chaoliu/Documents")
path = os.getcwd()
print(path)


# t = os.open("git.txt", os.O_RDWR | os.O_CREAT)
# b = str.encode("uuuu")
# os.write(t, b)
# os.close(t)


# 查看目录中的内容,并把目录中的内容返回一个列表
t = os.listdir("/Users/chaoliu/Documents")
for i in t:
    print(i)

# remove需要权限
os.remove("/Users/chaoliu/Documents/uuuu")

