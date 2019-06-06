# author: bavdu
# email: bavduer@163.com
# date: 2019/06/06
# usage: study functions advanced.


# TrainExam: define functions and used.
def makelist(number=2):
    return [i for i in range(number)]


list01 = makelist(10)
print(list01)


def readfile(path, mode, content=None):
    '''
    根据用户输入的路径和模式对文件进行读和写
    :param path: 规定好要操作的文件路径
    :param mode: 模式与open()保持一致
    :param content:  文件的内容,但当用户想要读文件时,content为空
    '''
    if mode == "r" or mode == "r+":
        with open(path, mode) as file:
            for line in file.readlines():
                print(line)
    else:
        with open(path, mode) as file:
            file.write(content)


help(readfile)







