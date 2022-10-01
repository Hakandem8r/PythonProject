score = int(input("please enter your score: "))

x = 5
if x > 4:
    x = x + 1

if x > 5:
    x = x + 2

if x > 7:
    x = x + 3
print("x ", x)

print("-------------------------------------------")

salary = float(input("please enter your salary: "))

if salary < 0:
    print("Invalid Value")
else:
    if 0 < salary <= 1000:
        salary = salary + salary * 0.15
    elif salary <= 2000:
        salary = salary + salary * 0.1
    elif salary <= 3000:
        salary = salary + salary * 0.05
    else:salary = salary + salary * 0.025

    print("you raised salary is ", salary)