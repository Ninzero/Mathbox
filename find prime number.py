#!/user/bin/python
import math
while 1==1:
    count=0
    n=int(input("请输入你希望倒序查找的素数开始"))
    for a in [n-x for x in range(n)]:
        for b in [x+2 for x in range(math.ceil(math.sqrt(a)))]:
            if a/b == int(a/b):
                break
            if b==math.ceil(math.sqrt(a)):
                print (a)
                count=count+1
        if count == 10:
            break
