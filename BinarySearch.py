myList = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
upperBound = 9
lowerBound = 0
index = 0
item = int(input("Please enter item to be found: "))
found = False

while not found and lowerBound <= upperBound:
    index = (upperBound + lowerBound) // 2

    if item == myList[index]:
        found = True
    elif item > myList[index]:
        lowerBound = index + 1
    else:
        upperBound = index - 1

if found:
    print("Item found")
else:
    print("Item not found")