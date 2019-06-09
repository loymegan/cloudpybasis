# author: bavdu
# email: bavduer@163.com
# date: 2019/06/09
# usage: define class


# 定义一个盒子类
class Box:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

    def getArea(self):
        area = (self.length * self.width) + (self.length * self.height) + (self.width + self.height)
        return area * 2

    def getCir(self):
        volume = self.length * self.width * self.height
        return volume


# 实例化一个盒子
carton = Box(5, 3, 2)

# 调用类中的方法
Area = carton.getArea()
Volume = carton.getCir()
print("area: %d, volume: %d" % (Area, Volume))
