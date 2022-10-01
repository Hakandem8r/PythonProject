
print("a" in "Hakan")

#for "i" in "Hakan";
    #print(i)

print("----------------in-------------------")
print(5 in [1,2,3,4])
print(5 not in [1,2,3,4])

print("a" in "Hakan")
print("z" in "Hakan")

print("---------------def------------------")
def nums (*a):
    for n in a:
        print(n, end=", ")

    nums(1,2,3)

print("----------------def2-----------------")
def bilgi(**a):
    for x in a:
        print(a["name"])
        print(a["age"])

bilgi(name="adi", age=20, surname="soyadi") #Virgül, peşpeşe birer boşluk bırakarak yazdır

print(".......................................")

List = [1,2,3]

print(list)
print(*list) # başına bir yıldız attığımızda birer boşluk bırakır

a="python"
print(a)
print(*a) # başına bir yıldız attığımızda birer boşluk bırakır

print("--------------------------------------")

#(a*5)
print(a*5)