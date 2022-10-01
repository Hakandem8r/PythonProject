people = [
    {"name":"Harry", "house":"Istanbul"},
    {"name":"Hakan", "house":"Berlin"},
    {"name":"Tom", "house":"Paris"}
]

# def f(person):
#     return person["name"]
# 
# people.sort(key=f)    OR

people.sort(key=lambda person: person["name"])

print(people)