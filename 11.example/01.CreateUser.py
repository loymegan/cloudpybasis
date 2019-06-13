# create user.
# date: 2019/06/13

import sys
import os
username = input('UserName: ')
if len(username) == 0:
    print('Warning: your must input username!!!')
    sys.exit(110)
else:
    os.system('useradd {}'.format(username))
    password = input('PassWord: ')
    if len(password) == 0:
        os.system('echo 123456 | passwd --stdin {}'.format(username))
    else:
        os.system('echo {} | passwd --stdin {}'.format(password, username))
