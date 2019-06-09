# author: bavdu
# email: bavduer@163.com
# date: 2019/06/09
# usage: class method


class Service:
    SERVICE_NAME = "Service Name is {}"
    def __init__(self, name, configfile, port):
        self.name = name
        self.__configfile = configfile
        self.port = port

    @classmethod
    def createService(cls, name, port):
        return cls(name=name, configfile="nothing", port=port)

    def getPort(self):
        return self.port

    @staticmethod
    def getConfigure(context):
        return Service.SERVICE_NAME.format(context)


# 使用类函数创建一个服务
MySQL = Service.createService("MySQL", 3306)

# 使用成员函数来获取服务的信息
print(MySQL.getPort())

# 使用静态方法来打印想要打印的信息
print(Service.getConfigure("this is a database service."))

