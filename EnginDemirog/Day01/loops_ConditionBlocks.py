dolarYesterday = 7.35
dolarToday = 7.35

# syntax : kod yazımı
# indentation : belli bir boşluk bırakma
if dolarYesterday > dolarToday:
    print("Decrease image")

if dolarYesterday < dolarToday:
    print("Increase image")

print("----------------------------------------------")

if dolarYesterday > dolarToday:
    print("Decrease image")
else:
    print("Increase image")

print("----------------------------------------------")

if dolarYesterday > dolarToday:
    print("Decrease image")
elif dolarYesterday < dolarToday:  # elif => else if
    print("Increase image")
elif dolarYesterday == dolarToday:
    print("No change image")

    #todo=> Python's blocks are if, else, elif
