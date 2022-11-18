# recurssive approach
# import math
# pr = [20, 15, 10]
# wei = [10, 7, 3]
# N = len(pr)
# W = 10


# def maxProfit(idx, wt):
#     if wt < 0:
#         return -math.inf
#     if wt == 0 or idx < 0:
#         return 0
#     return max(maxProfit(idx-1, wt), pr[idx] + maxProfit(idx-1, wt - wei[idx]))


# print(maxProfit(N-1, W))


import math
pr = [20, 15, 10]
wei = [10, 7, 3]
N = len(pr)
W = 10

ans = [[-1 for i in range(W+1)] for i in range(N)]


def maxProfit(idx, wt):
    if wt < 0:
        return -math.inf
    if wt == 0 or idx < 0:
        return 0
    if ans[idx][wt] != -1:
        return ans[idx][wt]
    ans[idx][wt] = max(maxProfit(idx-1, wt), pr[idx] +
                       maxProfit(idx-1, wt - wei[idx]))
    return ans[idx][wt]


print(maxProfit(N-1, W))
