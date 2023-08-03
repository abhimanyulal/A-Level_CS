myList = [4,2,5,16,45,1,32,46,94]
item = int(input("please enter item to be found"))
found = False
index = 0
while index <(len(myList)) and (found == False):
    if(myList[index] == item):
        found = True
    index = index + 1
if(found == True):
    print("item found")
else:
    print("Item not found")
 