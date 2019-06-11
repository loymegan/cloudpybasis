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

# 查看当前目录的绝对路径
path = os.getcwd()
print(path)

# 查看指定目录下包含的文件,返回一个列表
file = os.listdir(path)
print(file, type(file))

# 获取一个文件所在的目录名
dirname = os.path.dirname("/etc/yum.repos.d/CentOS-Base.repo")
print(dirname)

# 获取一个路径中的文件名
filename = os.path.basename("/etc/yum.repos.d/CentOS-Base.repo")
print(filename)

# 获取一个路径下的目录和文件名字,返回一个元组
path = os.path.split("/etc/yum.repos.d/CentOS-Base.repo")
print(path)

# 把目录与文件进行拼接
path = "/etc/yum.repos.d"
file = "nginx.repo"
p = os.path.join(path, file)
print(p)

# 获取文件的绝对路径
abspath = os.path.abspath("/hosts")
print(abspath)

# 查找文件
import fnmatch
print(os.listdir('.'))

path = [file for file in os.listdir('.') if fnmatch.fnmatch(file, '*.py')]
print(path)
