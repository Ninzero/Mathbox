#!/user/bin/python
import math


def lef(x):    # 用于计算出方程左边的值，函数righ同理
    l=x*x-13/4
    return l


def righ(x):
    r=math.sqrt(5)*x
    return r


def judge(a, b, c, d, e):  # 用于判断是否是方程的解
    x = (a * math.sqrt(b) + c * math.sqrt(d)) / e
    left = lef(x)
    right = righ(x)
    if abs(left - right) < 0.000000001:
        print("x=(", a, "*√", b, "+", c, "*√", d, ")/", e)
        return 1
    else:
        return 0


def mathbox(m,n):   # 函数主体，m、n用于限制循环范围
    for a in [x for x in range(m+1)]:
        for b in [x+1 for x in range(n)]:
            for e in [x+1 for x in range(m)]:
                for c in [x for x in range(m+1)]:
                    for d in [x+1 for x in range(n)]:
                       answer = 0
                       answer = judge(a, b, c, d, e)
                       if answer == 1:
                           return
                       c = 0-c
                       answer = judge(a, b, c, d, e)
                       if answer == 1:
                           return
                       a = 0-a; c = 0-c
                       answer = judge(a, b, c, d, e)
                       if answer == 1:
                           return
                       c = 0 - c
                       answer = judge(a, b, c, d, e)
                       if answer == 1:
                           return

mathbox(20, 20)