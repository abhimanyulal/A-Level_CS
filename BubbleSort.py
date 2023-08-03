myList = [7, 3, 9, 2, 1, 5, 4, 6, 8]
upperBound = 8
lowerBound = 0
index = 0
swap = True
temp = 0
top = upperBound

while (swap) and (top > 0):
    swap = False
    for index in range(top-1):
        if myList[index] > myList[index + 1]:
            temp = myList[index]
            myList[index] = myList[index + 1]
            myList[index + 1] = temp
            swap = True
    top = top -1

print("Sorted list:")
print(myList)