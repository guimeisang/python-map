# coding=utf-8

import os;

file = open('demo.txt', 'w');
print "文件名", file.name;
file.write("我开始写入了哈哈哈哈ha");
print file.tell();
# 输出当前指针的位置
file.seek(os.SEEK_SET);
# 设置指针回到文件当初
context = file.read();
print context;
file.close();