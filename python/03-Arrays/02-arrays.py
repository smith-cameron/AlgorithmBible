#1 - Array: Min to Front
def minFront(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
            idx = i
    for i in range(idx, 0, -1) :
        temp = list[i]
        list[i] = list[i-1]
        list[i-1] = temp
    return list
#myList = [4,2,1,3,5,6]
#print(minFront(myList))

#2 - Array: Reverse
def reverse(list):
    for i in range(len(list)//2):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list
# print(reverse([4,2,1,3,5]))

#3 - Array: Rotate 
def getShwifty(list, shift):
    if shift < 0:
        print(f"Shift Left by: {shift*-1}")
        for i in range(shift*-1):
            temp = list[0]
            # print(f"outerLoopTemp: {temp}")
            # print(f"outerLoopList: {list}")
            for i in range(0, len(list)-1, +1):
                list[i] = list[i+1]
                # print(f"innerLoopList: {list}")
            list[len(list)-1] = temp
    if shift > 0:
        print(f"Shift Right by: {shift}")
        for i in range(shift):
            temp = list[len(list)-1]
            # print(f"outerLoopTemp: {temp}")
            # print(f"outerLoopList: {list}")
            for i in range(len(list)-1, 0, -1):
                list[i] = list[i-1]
                # print(f"innerLoopList: {list}")
            list[0] = temp
    if shift == 0:
        print("No Shift")
    return list
print(f"output: {getShwifty([1,2,3,4,5,6,7,8,9,10,11,12,13],-5)}")

#4 - Array: Filter Range
def filterByRange(list, min, max):
    for j in range(len(list)-1):
        if list[j] > min and list[j] < max:
            sel = list[j]
            for i in range(sel-1, len(list)-1):
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
            list.pop(len(list)-1)
    return list
#print(filterByRange([1,2,3,4,5,6,7,8,9], 3, 5))

#5 - Array: Concat
def concat(list, list2):
    return list + list2
#print(concat(['a','b'], [1,2]))

#6 - Skyline Heights
def skyline(list):
    newList = []
    for i in range(len(list)-1):
        if list[i] > 0:
            currentValue = list[i]
            if len(newList) == 0:
                newList.append(currentValue)
            else:
                if currentValue <= newList[len(newList)-1]:
                    continue
                else:
                    newList.append(currentValue)
    return newList
#print(skyline([-1,7,3]))