finalStr = ""
givenStr = "Hello, Global AI Hub!"

for i in givenStr:
    if i != "I":
        finalStr += i
    else:
        break

print(finalStr)

print("---------------------------------")
#If we enter 50 for score, what will the output be?

currentList = ["Hello", "World"]
finalList = []

for i in currentList:
    for j in i:
        finalList.append(j)

print(finalList)

print("---------------------------------")
# What is the output?

yourName = "Global AI Hub".split()

if (yourName[0] != yourName[1]) and (yourName[1] == yourName[2]):
    print(yourName[0])
else:
    print("Global AI Hub")

print("---------------------------------")
# Which of the following options would represent the correct output
# of the given code snippet?

isFalse, isTrue = True, False
isFalse, isTrue = isTrue, isFalse

if ((isFalse != isTrue) and (isTrue) or (isFalse)):
    print("True")
else:
    print("False")

print("---------------------------------")
# What would the following code produce as a result?

#i = 2

#while i != 15:
   # print(i)
   # i += 2  #InfiniteLoop 2, 4, 6, 8

print("---------------------------------")
# What is the correct output of the given code?
randomList = ["1", "2", "3"]
print(randomList[0] + randomList[2])

print("---------------------------------")
# What is the correct output of the given code?

customList = [i ** 2 for i in range(5)]
print(max(customList))

print("---------------------------------")

# What is the correct output of the given code?
x = 11

if (float(x) == x):
    print(f"{float(x)} is equal to{x}")
else:
    print(f"{float(x)} is not equal to {x}")

print("---------------------------------")
# What is the correct output of the given code?

customList = list(range(10,20,2))

totalOdds = 0
totalEvens = 0

for i in customList:
    if i % 2 == 0:
        totalEvens += 1
    else:
        totalOdds += 1

print(f"Total Evens: {totalEvens}; Total Odds: {totalOdds}")


