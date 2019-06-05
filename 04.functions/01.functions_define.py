# author: bavdu
# email: bavduer@163.com
# date: 2019/06/05
# usage: define functions


# 普通函数的定义.
def echoln01():
    print("hello world")

# def: 可执行语句,当函数被调用时才生效,不被调用时是不会运行的
# echoln: 函数名
# (): 括号,作用可以包含传进函数内部的参数
# 函数主体: 该函数实现某个功能的代码

# 定义带参数的函数.
def echoln02(m):
    print(m)


def echoln03(m=0):
    print(m)


# 定义带返回值的函数.
def echoln04(pge="string"):
    return pge


# 函数的调用.
op = echoln04()
print(op)


# 把打开文件的方式集成到一个函数内部, 函数的参数为文件的路径, 调用函数时,
# 可以直接利用file调用readlines方法

def openfile(path):
    with open(path, "r+") as file:
        return file


f = openfile("./information")

# 01.实现一个加法函数Mysum, 可以传进两个参数, 让这两个参数进行相加.
def Mysum(a, b):
    print(a + b)


Mysum(10, 45)

# 02.实现一个大小写转换的函数Myupper, 可以把字符串传进去返回一个全部被转换大写的字符串
def Myupper(string):
    print(string.upper())


Myupper("abc")

# 03.实现一个对列表排序的函数Mysorted, 输入一个列表进去, 可以把列表中的数字进行排序
def Mysorted(list):
    list.sort()
    print(list)


Mysorted([1, 9, 2, 4, 3])








