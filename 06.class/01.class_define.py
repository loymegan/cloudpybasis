# 类: 箱子类
# 属性(特征): 有长度、有宽度、有高度、生产方、材料
# 方法(根据属性能够得到的值或者行为): 获取箱子的面积、获取箱子的体积、获取生产方、获取材质


# class: 女朋友
# attribute: 耍小脾气、买买买、身高、体重、颜值
# functions: 撒娇、花钱、穿衣服、化妆、吃、做饭、会打人、咬人


# 女朋友("买买买", "身高172", "体重60kg", "颜值99")
# 女朋友.撒娇("一哭二闹三上吊")


# 声明一个类
class Box:
    def __init__(self, length, width, high):
        self.length = length
        self.width = width
        self.high = high

    def getArea(self):
        area = self.length * self.width + self.length * self.high + self.width * self.high
        return area * 2

    def getVolume(self):
        volume = self.length * self.width * self.high
        return volume


# 实例化
paperBox = Box(21.4, 10.8, 9.5)

# 调用类中的方法
paperBox_volume = paperBox.getVolume()
print(paperBox_volume)









