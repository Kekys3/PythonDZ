#from datetime import date
#ur = date.today().year
#def century_message(a, b, c):
#    v = 100 - int(b)
#    g = v + c
#    ur = date.today().year
#    return f"{a} ,тебе исполняется 100 лет в {g} году"
#m = (input("Введите ваш возраст"))
#k = (input("Введите ваше имя:"))
#print(century_message(k,m,ur))

from datetime import date
def century_message(a, b, c):
    v = 100 - int(b)
    g = v + int(c)
    return f"{a} ,тебе исполняется 100 лет в {g} году"
m = (input("Введите ваш возраст"))
k = (input("Введите ваше имя:"))
o = (input("Нынешний год:"))
print(century_message(k,m,o))