# coding: utf-8
# author: bavdu
# email: bavduer@163.com
# date: 2019/06/01
# usage: print list's index.


list01 = [1, 2, 3, 4, 1, 1, 6, 1, 4, 1]
for index in range(len(list01)):
    if list01[index] == 1:
        print(index)
