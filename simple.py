#!/user/bin/python
import math
import time
def my_try (answer):
    for c in [x+1 for x in range(100)]:
        for b in [x+1 for x in range(100)]:
            for a in[x for x in range(101)]:
                result = (b*math.sqrt(a))/c
                if abs(result-abs(answer))<0.000000001:
                    print ('(',b,'*','sqrt',a,')','/',c)
                    return
while 1==1:
    d=float(input("请输入小数："))
    now1 = time.time()
    my_try(d)
    now2 = time.time()
    print ("本次计算大约用时",now2-now1,"秒")