N = 24151
ways = [-1 for i in range(N+1)]


def total_ways(i):
    if i > N:
        return 0
    if i == N:
        return 1
    if ways[i] != -1:
        return ways[i]
    ways[i] = total_ways(i+1) + total_ways(i+2)
    return ways[i]


print(total_ways(0))
