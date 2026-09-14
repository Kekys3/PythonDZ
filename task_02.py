def bytes_to_kilobytes(a):
    return a / 1024
def kilobytes_to_bytes(b):
    return b * 1024
c = input("Что и куда переводим:")
if c == bytes_to_kilobytes:
    print(bytes_to_kilobytes(int(input(":Какое количество"))))
else:
    print(kilobytes_to_bytes(int(input("Какое количество:"))))
