list1 = list((1,2,3,4,5))
list2=list1
list3=list1.copy()

list1[-1] = 6
print(f"List 1: {list1}, {list2}, {list3}")

print("-----------------------------")

randomDict={1:"1", 2:["1","2"], 3:["1","2","3"]}

for key, value in randomDict.items():
    for v in value:
        print(v, end=" ")

print("-----------------------------")

customTuple = (10,20,40,30,50)
customTuple = customTuple[::-1]

for i in customTuple:
    print(i, end=" ")

print("-----------------------------")

D={1 : 1, 2 : '2', '1' : 2, '2' : 3}
D['1'] = 2
print(D[D[D[str(D[1])]]])

print("-----------------------------")

customDict = {i: i * i for i in range(5)}
print(customDict)

print("-----------------------------")

givenList = [x if x%2 else x*100 for x in range(1,5)]
print(givenList)