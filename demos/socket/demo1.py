#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket

s = socket.socket()

host = socket.gethostname();
port = 12345

s.bind((host, port));

s.listen(5)
while True:
    c, addr = s.accept()
    c.send('欢迎访问哈哈哈')
    c.close()