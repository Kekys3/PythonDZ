def index_of_min(a):
    if not a:
        return -1
    return a.index(min(a))
print(index_of_min([]))