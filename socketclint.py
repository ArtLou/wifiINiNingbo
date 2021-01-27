#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import time
n=1
#reload(sys)
#sys.setdefaultencoding('utf8')
import socket# 客户端 发送一个数据，再接收一个数据
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
client.connect(('localhost',2020)) #建立一个链接，连接到本地的6969端口
while True:

    # addr = client.accept()
    # print '连接地址：', addr
    msg = '小楼的第'+str(n) +'次测试'  
    client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
    data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
    print('recv:',data.decode()) #输出我接收的信息
    time.sleep(1)
    n=n+1
client.close() #关闭这个链接