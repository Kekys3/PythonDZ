def multiplication_table(a):
    c = []
    for i in range(1, 11):
        c.append(f"{a} x {i} = {a * i}")
    return c
print(multiplication_table(10))