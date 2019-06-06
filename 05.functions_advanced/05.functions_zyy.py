# author: bavdu
# email: bavduer@163.com
# date: 2019/06/06
# usage: study functions zyy


# # 函数作用域: 局部变量和全局变量
# # 局部变量
# def func01(number):
#     result = number + 1
#     return result
#
# # func01(10)
# # print(result)
#
# # 全局变量
# result = 100
# def func02():
#     print(result)
#
# func02()
#
#
# # 局部变量在函数外部的调用方法
# def func03(number):
#     global result
#     result = number + 1
#     return result
#
# func03(11)
# print(result)


# 声明全局变量后声明局部变量
# 在函数中使用的局部变量的名称与全局变量的名称相同.
result = 112233
def func04():
    result = 334455
    print(result)


func04()
print(result)













