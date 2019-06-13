#!/usr/bin/env bash
#
# author: bavdu
# email: bavduer@163.com
# date: 2019/06/13


#ip=192.168.4
#n=2
#while ((n<254))
#do
#
#ping -c 1  ${ip}.${n} >> /dev/null
#if [ $? -eq 0 ];then
#  echo "${ip}.${n}  online"
#else
#  echo "${ip}.${n}  down"
#fi
#let n++
#done



ip='192.168.3'
for i in $(seq 2 254)
do
    {
        ping -c1 -i 0.01 ${ip}.${i} &>/dev/null
        if [ $? -eq 0 ];then
            echo '${ip}.${i} up'
        else
            echo '${ip}.${i} down'
        fi
    }&
done



