# author: bavdu
# email: bavduer@163.com
# date: 2019/06/06
# usage: functions qt


# 5 --> 5*4*3*2*1
# 5 --> 5+4+3+2+1
def Jc(number):
    Sum = 0
    if type(number) == int:
        for i in range(1, number+1):
            Sum += i
        return Sum
    else:
        return "shit"


def Jc02(number):
    if type(number) != int:
        return "shit"
    elif number < 0:
        return "shit"
    elif number == 0:
        return 0
    def Jc03(number):
        n, Sum = 1, 0
        while n <= number:
            Sum += n
            n+= 1
        return Sum
    print(Jc03(number))


Jc02(10)
