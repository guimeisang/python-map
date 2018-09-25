#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time

# 定义函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))


try:
    thread.start_new_thread(print_time, ("111", 2))
    thread.start_new_thread(print_time, ("222", 4))
except:
    print "Error: unable to start thread"

while 1:
    pass