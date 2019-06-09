# author: bavdu
# email: bavduer@163.com
# date: 2019/06/09
# usage: class atrribute.


class Server:
    def __init__(self, cpu, memory, disk, network):
        self.cpu = cpu
        self.__memory = memory  # 私有属性,防止在类外被修改
        self.disk = disk
        self.network = network

    def cpuUsageRate(self):
        if self.cpu <= 16:
            print("this server cpu usage rate: 60%")

    def memoryUsageRate(self):
        if self.__memory <= 128:
            print("this server memory usage rate: 80%")

    def diskUsageRate(self):
        if self.disk <= 6000:
            print("this server disk usage rate: 90%")

    def networkUsageRate(self):
        if self.disk >= 1000:
            print("this server network usage rate: 100%")


dell_r710 = Server(12, 64, 4000, 10000)

# 改变类中的属性值
dell_r710.cpu = 100

# 调用私有属性及类属性
print(dell_r710.cpu)
print(dell_r710.cpu, dell_r710.memory, dell_r710.disk, dell_r710.network)




