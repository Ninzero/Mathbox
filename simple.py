#!/user/bin/python
import math
import time
def my_try (answer):
    for c in [x+1 for x in range(1000)]:
        for b in [x+1 for x in range(1000)]:
            for a in[x for x in range(1001)]:
                result = (b*math.sqrt(a))/c
                if abs(result-abs(answer))<0.0000001:
                    print ('(',b,'*','sqrt',a,')','/',c)
                    return
while 1==1:
    d=float(input())
    now1 = int(time.time())
    my_try(d)
    now2 = int(time.time())
    print (now2-now1)