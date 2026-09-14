def month_calendar(a, b):
    result = ""
    for day in range(1, b + 1):
        if day == 1:
            result += "   " * a
        result += f"{day:2}"
        if (day + a) % 7 == 0:
            result += "\n"
        else:
            result += " "
    return result.rstrip()
print(month_calendar(6, 25))