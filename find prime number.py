#!/user/bin/python
import math
count=0
for a in [1000-x for x in range(1000)]:
    for b in [x+2 for x in range(math.ceil(math.sqrt(a)))]:
        if a/b == int(a/b):
            break
        if b==math.ceil(math.sqrt(a)):
            print (a)
            count=count+1
    if count == 10:
        break
