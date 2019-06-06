# author: bavdu
# email: bavduer@163.com
# date: 2019/06/06
# usage: study functions nm


# def jx(number):
#     print(number)
#
# a = jx()
# print(a(3))


# y = ax + b
# x = x**2

# lambda 参数01, 参数02: 表达式
t = lambda x: x**2
print(t(3), type(t))

# 在列表生成式中应用来；lambda
list01 = [(lambda i: i**3)(i) for i in range(10)]
print(list01)
print(len(list01))


# list02 = [i for i in range(10) i = i**2]
def func01(number, n):
    return number**n
list02 = [func01(i, 2) for i in range(10)]
print(list02)









