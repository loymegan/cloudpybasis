# 1. 根据用户输入的出生年份换算出用户的属相
# 2. 根据用户输入的生日换算出用户的星座.


shuxiang = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
xingzuo = ((1, 20), (2, 19), (3, 21), (4, 20), (5, 21), (6, 22),
           (7, 23), (8, 23), (9, 23), (10, 24), (11, 23), (12, 22))
xingzuoming = ("水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座",
               "狮子座", "处女座", "天秤座", "天蝎座", "射手座", "摩羯座")


year = int(input("请输入你出生的年份: "))
month = int(input("请输入你的出生月份(1~12): "))
day = int(input("请输入你的出生日期(1~31): "))

print(shuxiang[year % 12])
list01 = []
for i in range(len(xingzuo)):
    if xingzuo[i] < (month, day):
        list01.append(xingzuo[i])
print(xingzuoming[len(list01) - 1])



