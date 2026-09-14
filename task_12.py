def shortest_distance(k, m):
    a = k * 1000
    if a < m:
        return a
    else:
        return m
print(shortest_distance(3, 5000))