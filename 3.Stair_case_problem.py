# Brute force using recurssion
# Time complexity: O(2^n)
# N = 5
# def func(x):
#     if x > N:
#         return 0
#     if x == N:
#         return 1
#     return func(x+1) + func(x+2)
# print(func(0))

# top down
N = 3
temp = [-1 for i in range(N+1)]


def func(x):
    if x > N:
        return 0
    if x == N:
        return 1
    if temp[x] != -1:
        return temp[x]
    temp[x] = func(x+1) + func(x+2)
    return temp[x]


print(func(0))
