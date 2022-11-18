from glob import glob
import math

wt = [10, 20, 30]
W = 50
p = [60, 100, 120]
N = len(p)
ans = [[-1 for i in range(N)] for j in range(W+1)]


def func(x, ind):
    global ans
    if x < 0:
        return -math.inf
    if x == 0 or ind < 0:
        return 0
    if ans[x][ind] != -1:
        return ans[x][ind]
    ans[x][ind] = max(p[ind]+func(x-wt[ind], ind-1), func(x, ind-1))
    return ans[x][ind]


print(func(W, 2))


