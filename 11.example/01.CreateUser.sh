#!/usr/bin/env bash
#
# author: bavdu
# email: bavuer@163.com
# date: 2019/06/13
# create user.


read -p "UserName: " username
read -p "PassWord: " password

if [ -z ${username} ];then
    echo "Warning: your must input username!!!"
    exit 110
else
    useradd ${username}
    if [ -z ${password} ];then
        echo "123456" | passwd --stdin ${username}
    else
        echo "${password}" | passwd --stdin ${username}
    fi
fi