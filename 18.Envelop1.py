import math


w = [(4, 2), (5, 3), (1, 3), (6, 3), (2, 4), (3, 5)]
# w = [(10, 12), (19, 14), (15, 100)]
N = len(w)
w.sort()
# Longest increasing pair
LIP = [-1 for i in range(N)]
ans = -math.inf
for i in range(N):
    LIP[i] = 1
    for j in range(0, i):
        # Base condition
        if w[i][0] > w[j][0] and w[i][1] > w[j][1]:
            LIP[i] = max(LIP[i], 1+LIP[j])
    ans = max(ans, LIP[i])
print(ans)
