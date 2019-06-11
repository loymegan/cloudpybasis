# 类的继承
class Box():
    def __init__(self, length, width, high):
        self.length = length
        self.width = width
        self.high = high

    def getArea(self):
        area01 = self.length * self.width
        area02 = self.length * self.high
        area03 = self.width * self.high
        area = (area01 + area02 + area03) * 2
        return area

    def getVolume(self):
        volume = self.length * self.width * self.high
        print("Box's getVolume", volume)


class PaperBox(Box):
    def __init__(self, cl, length, width, high):
        super().__init__(length, width, high)
        self.cl = cl

    def getVolume(self):
        area = self.length * self.width
        volume = area * self.high
        print("PaperBox's getVolume", volume)


box01 = PaperBox("paper", 21.5, 10.9, 9.5)
box01.getVolume()




