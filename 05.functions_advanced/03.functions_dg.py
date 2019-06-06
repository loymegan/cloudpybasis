# author: bavdu
# email: bavduer@163.com
# date: 2019/06/06
# usage: functions dg


# number = int(input("Please number: "))
# n, jc = 1, 1
# while n <= number:
#     jc *= n
#     n += 1
# print(jc)

def dog(number):
    if number != 0:
        result = number * dog(number-1)
    else:
        return 1
    return result


print(dog(10))
