def days_in_month(a, b):
    if a in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif a in (4, 6, 9, 11):
        return 30
    else:
        if (b % 400 == 0) or (b % 4 == 0 and b % 100 != 0):
            return 29
        return 28
print(days_in_month(2,2000))

