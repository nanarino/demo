#!/usr/bin/env python
# -*- coding: utf-8 -*-


def foo():
    step = 0

    def move(n, home="A柱", destination="C柱", assistance="B柱"):
        nonlocal step
        if n == 1:
            step += 1
            print("\t第%d步:将" % step + home + "的最上面的环移动到" + destination +
                  "的最上面")
        if n > 1:
            move(n - 1, home, assistance, destination)
            move(1, home, destination, assistance)
            move(n - 1, assistance, destination, home)

    return move


while 1:
    print("\t")
    print("\t请输入需要移动的汉诺塔的层数(最好是个位数)")
    print("\t无输入或者输入0退出")
    temp = input("\t请按数字键输入:")
    if not temp:
        break
    temp = int(temp)
    if not temp:
        break
    foo()(temp)
