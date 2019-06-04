# author: bavdu
# email: bavduer@163.com
# date: 2019/06/04
# usage: file output info


# 第一道题: 把文件中的信息输出到下面的字典中
information = {
    "China":
        {
            "URL": None,
            "UserName": None,
            "PassWord": None
        },
    "Sydney":
        {
            "URL": None,
            "UserName": None,
            "PassWord": None
        },
    "NewYork":
        {
            "URL": None,
            "UserName": None,
            "PassWord": None
        }
}


# 第二道题: 取到"1T"
info = []
info.append(
    {'192.168.1.11':
         {'cpu': ['Intel(R) Core(TM) i5-5350U CPU @ 1.80GHz', 4, 1],
          'memory': ['16', '4', '2'],
          'disk': ['1T', '2T']
         }
    })

info.append({
    '192.168.1.12': {
         'cpu': ['Intel(R) Core(TM) i5-5350U CPU @ 1.80GHz', 4, 1],
         'memory': ['16', '4', '2'],
         'disk': ['1T', '2T']
    }
})

