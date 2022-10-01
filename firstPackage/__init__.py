for i in [1, 2, 3, 4, 5]:
    print(i, end=", ")

print()

str = "hello python"
for c in str:
    print(c, end=" ")

print()
print(str[0])
print(str[0:4])
print(str[1:8:2])

# [baslama, bitis[dahil degil], artim]

list = [1,2,3,4,5,6,7,8,9,10]
print(list)
print(list[3])
print(list[3:8])
print(list[2:8:2])
print(list[3:])

liste1 = list[2:8]
print(liste1)
liste1[1]=10
print(liste1)

print(list[::-1])
print(list[::-2])
print(list[8:3:-2])
print(str[::-1])
print("Hello World"[::-1])