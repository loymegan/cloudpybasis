class Car:
    def __init__(self, brand, color, zj, yh, price, engine, bsx, dp):
        print("Run __init__()....")
        self.brand = brand
        self.color = color
        self.zj = zj
        self.yh = yh
        self.price = price        # 属性的私有化--搭配__init__()函数使用时叫做类的封装
        self.engine = engine
        self.bsx = bsx
        self.dp = dp

    def getPrice(self):
        return self.price

    def getZj(self):
        return self.zj


BMW3 = Car("BMW", "yellow", "2910mm", 6.8, 319800, "B48B20N", "ZF-8AT", "G20")


