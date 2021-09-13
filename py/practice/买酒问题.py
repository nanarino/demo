import time
"""
十块钱买五瓶啤酒四个瓶盖换一瓶，两个空瓶换一瓶，请十块钱可以喝多少瓶啤酒
"""


def 边喝边买(钱, 瓶盖=0, 空瓶=0, 酒=0):
    def 钱换酒(a):
        nonlocal 钱
        nonlocal 瓶盖
        nonlocal 空瓶
        nonlocal 酒
        if a >= 2:
            time.sleep(1)
            钱 %= 2
            瓶盖 += (a // 2)
            空瓶 += (a // 2)
            酒 += (a // 2)
            print("买了%d瓶酒" % (a // 2))

    def 瓶盖换酒(a):
        nonlocal 瓶盖
        nonlocal 空瓶
        nonlocal 酒
        if a >= 4:
            time.sleep(1)
            瓶盖 %= 4
            瓶盖 += (a // 4)
            空瓶 += (a // 4)
            酒 += (a // 4)
            print("换了%d瓶酒" % (a // 4))

    def 空瓶换酒(a):
        nonlocal 瓶盖
        nonlocal 空瓶
        nonlocal 酒
        if a >= 2:
            空瓶 %= 2
            瓶盖 += (a // 2)
            空瓶 += (a // 2)
            酒 += (a // 2)
            print("换了%d瓶酒" % (a // 2))

    钱换酒(钱)
    while 1:
        空瓶换酒(空瓶)
        瓶盖换酒(瓶盖)
        if 瓶盖 < 4 and 空瓶 < 2:
            break
    print("一共喝了%d瓶酒" % 酒)


边喝边买(10)