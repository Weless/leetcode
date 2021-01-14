from typing import List

import random
import time

res = []
def produceRandomNum(n):
    if n <= 0:
        return
    random.seed(time.time())
    alist = list(range(n))
    while alist:
        x = random.choice(alist)
        res.append(x)
        alist.remove(x)
n = 1
produceRandomNum(n)
# print(res)


def check(res,n):
    if n <= 0:
        return res == []
    if len(res) != n:
        return False
    for i in range(0,n):
        if i not in res:
            return False
    return True
