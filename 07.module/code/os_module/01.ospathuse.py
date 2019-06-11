
import os

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

