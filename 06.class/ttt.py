
import sys


class Box:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def getArea(self):
        area01 = self.l * self.w
        area02 = self.l * self.h
        area03 = self.w * self.h
        return (area01 + area02 + area03) * 2

    def getVolume(self):
        return self.l * self.w * self.h


paperBox = Box(20, 10, 5)

volume = paperBox.getVolume()
print(volume)
area = paperBox.getArea()
print(area)


class PaperBox(Box):
    def __init__(self, l, w, h, color):
        super(PaperBox, self).__init__(l, w, h)
        self.color = color

    def getColor(self):
        return self.color

    def getArea(self, m):
        if type(m) != str:
            sys.exit(250)
        area = (self.l*self.w)*2 + (self.l*self.h)*2 + (self.w*self.h)*2
        return str(area) + " " + m


paperBox01 = PaperBox(21.4, 14.5, 5.6, "green")
color = paperBox01.getColor()
print(color)
volume = paperBox01.getVolume()
print("paperBox01's volume: %.2f" % (volume))
print("paperBox01's volume: %d" % (volume))
print("paperBox01's volume: %s" % (volume))

print("%.2f" % (volume))
def number(n):
    return "%.2f" % (n)
v = number(volume)
print("paperBox01's volume: {}".format(v))


paperBox02 = PaperBox(20, 10, 5, "red")
area = paperBox02.getArea("m^2")
print(area)



