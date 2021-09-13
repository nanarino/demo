#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
answer = random.randint(0, 99)
print("...请猜猜今天的幸运数字0~99...")
temp = input("请按数字键输入:")
guess = int(temp)
t = 1
while guess != answer:
    if guess > answer:
        print("...似乎猜得太大了...")
    else:
        print("...似乎猜得太小了...")
    temp = input("请按数字键再次输入:")
    guess = int(temp)
    t = t + 1
if t == 1:
    print("...夭寿了,一次就猜中了,太强了吧...")
elif t < 5:
    print("...居然只猜了%d次,今天很好运..." % t)
elif t > 15:
    print("...居然猜这么多次,你是傻子吗...")
else:
    print("...答对了,今天也是充满希望的一天...")
