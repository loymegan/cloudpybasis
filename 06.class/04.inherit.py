# author: bavdu
# email: bavduer@163.com
# date: 2019/06/09
# usage: class inherit


class Animal:
    def __init__(self, leg, mouse, eye):
        self.leg = leg
        self.mouse = mouse
        self.eye = eye
    
    def getLeg(self):
        return self.leg


class Dog(Animal):
    # def __init__(self, variety):
    #     # 继承父类中的属性,并对父类中的属性进行实例化
    #     Animal.__init__(self, leg=4, mouse="length", eye=2)
    #     self.variety = variety
    def __init__(self, leg, mouse, eye, variety):
        # 定义新的类并对原来的类中的属性进行实例化
        super().__init__(leg, mouse, eye)
        self.variety = variety

    # 在子类中添加新的方法
    def getVariety(self):
        return self.variety

    # 继承类中的方法,并对方法进行重写
    def getLeg(self):
        legNumber = "{} have {} leg".format(self.variety, self.leg)
        return legNumber


# dog = Animal(4, "length", 2)
golden = Dog(4, "length", 2, "golden hair dog")

print(golden.getVariety())
print(golden.getLeg())

