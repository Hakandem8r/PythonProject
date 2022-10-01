def func1(x): return  x**2
def func2(x): return x

for x in list(range(3)):
    print((lambda x: func1(x)*func2(x))(x), end=" ")

print("----------------------------------------")

def subtract(*num):
    a=100

    for number in num:
        a -= number
        return a

print(subtract(1, 10, 20, 13, 37))

print("----------------------------------------")

randomStr = "This is a custom string to be manipulated."
randomStr.replace('i', " ", 10)

print(randomStr)

print("----------------------------------------")

def randomFunc(x,y,z):
    x=y+z
    y=x+z
    z=x+y

print("----------------------------------------")

x = 15.0
y = 0.0

def man(x,y):
    try:
        return  x / y
    except ZeroDivisionError:
        return  x/1

    print(main(x,y))