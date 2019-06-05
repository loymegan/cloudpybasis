# author: bavdu
# email: bavduer@163.com
# date: 2019/06/05
# usage: check linux server's cpu info.


def cpuinfo(param):
    with open("cpuinfo", "r+") as file:
        for line in file.readlines():
            if param in line:
                return line


info = cpuinfo("cores")
print(info)

