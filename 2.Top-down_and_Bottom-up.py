# computing using recurssion
# Time complexity: O(2^n)
# def fibnocii(N):
#     if N < 2:
#         return N
#     return fibnocii(N-1) + fibnocii(N-2)

# print(fibnocii(6))


# Reducing the time complexity by using extra space to store computed values
N = 7
arr = [-1 for i in range(N+1)]
def func(n):
    if n < 2:
        return n
    if arr[n] != -1:
        return arr[n]
    arr[n] = func(n-1) + func(n-2)  #optimal sub-structure
    return arr[n]
print(func(N))
