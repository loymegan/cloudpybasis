# coding: utf-8
# author: bavdu
# email: bavduer@163.com
# date: 2019/06/01
# usage: study string.


# 字符串类型的变量定义.
variable = "this my girl friends."

# t h i s   m y   g i r  l     f  r  i  e  n  d  s  .
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# 遍历字符串
variableLen = len(variable)     # 求字符串的长度
for i in range(variableLen):
    print(variable[i])

# 遍历字符串, 打印字符串中的单个字符.
print("第11索引值为: ", variable[11])

# range问题(左闭右开区间).所取数值均为整数.
# 左闭右开区间 = [1...100) i先取“1”, ...., i取到99时.区间结束.
# range(1, 100): 1 <= i <= 99
# range(100): 0 <= i <= 99

# 字符串的切片.
# t   h   i   s       m   y       g   i   r   l      f  r  i  e  n  d  s  .
# 0   1   2   3   4   5   6   7   8   9   10  11  12 13 14 15 16 17 18 19 20
# -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(variable[13:])
print(variable[-1])
print(variable[-8:-1])
print(variable[-13:-9])
print("正索引和负索引: ", variable[-13:12])

var01 = "abcdefgc"
var02 = var01.replace("c", "C")
print(var02)

# 替换敏感字符.
var03 = input("please input your string: ")
if var03 == "canglaoshi":
    var04 = var03.replace("cang", "*")
    print(var04)
    print(var03)












