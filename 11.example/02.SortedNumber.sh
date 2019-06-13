#!/usr/bin/env bash
#
# author: bavdu
# email: bavduer@163.com
# date: 2019.06.13


read -p 'number01: ' n01
read -p 'number02: ' n02
read -p 'number03: ' n03

if [ $n01 -gt $n02 ];then
    tmp=${n01}
    n01=${n02}
    n02=${tmp}
fi
if [ $n02 -gt $n03 ];then
   tmp=${n02}
   n02=${n03}
   n03=${tmp}
fi
if [ $n01 -gt $n03 ];then
   tmp=${n01}
   n01=${n03}
   n03=${tmp}
fi
 echo "$n01,$n02,$n03"



