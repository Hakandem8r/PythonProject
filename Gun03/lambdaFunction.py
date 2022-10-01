def kare(a):
    return a**2

x = lambda n : n**2

print(x(5))

print("-----------------------------------")
def us(a,b):
    return a**b

print(us(2, 3))

print("---------------------------------------")

def us1(a):
    return lambda n : a**n

print(us1(2)(3))

x = us1(2)
print(x(3))