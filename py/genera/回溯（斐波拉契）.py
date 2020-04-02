'''李老师爬楼梯，他每次可以走1级或2级，
输入楼梯的级数，求不同的走法数'''

import math, time


#全排列法 假设全是每步1级 一次次地将2级合并成1级 就全排列一次 直到每步都是2级
def permuta(step: int) -> int:
    m = 0
    sln = 0
    while step >= 0:
        sln += math.factorial(step +
                              m) / math.factorial(step) / math.factorial(m)
        step -= 2
        m += 1
    return int(sln)


#普通递归法 最后一步是1级或者2级 发现它和斐波拉契数列一样
def generecurs(step: int) -> int:
    if step <= 2:
        return step
    return generecurs(step - 1) + generecurs(step - 2)


#尾递归法 这里采用尾递归写法 避免大量重复计算
def tailrecurs(step: int, a1: int = 1, a2: int = 2) -> int:
    if step == 1:
        return a1
    if step == 2:
        return a2
    return tailrecurs(step - 1, a2, a1 + a2)


#通项公式法 已经知道它是斐波拉契数列数列 直接通项公式
def formula(step: int) -> int:
    s = math.sqrt(5)
    return int(
        (1 / s) * ((((1 + s) / 2)**(step + 1)) - (((1 - s) / 2)**(step + 1))))


#循环解构法 看起来是斐波拉契数列的最简洁写法 思路和尾递归方法一样
def cycle(step: int, a1: int = 1, a2: int = 2) -> int:
    for x in range(step - 1):
        a1, a2 = a2, a1 + a2
    return a1
