def guests_by_seat(a):
    n = len(a)
    c = [0] * n
    for k in range(n):
        guest = k + 1
        b = a[k]
        c[b - 1] = guest
    return c
print(guests_by_seat([11, 6, 8, 2, 10, 9, 4, 7, 3, 1, 5]))