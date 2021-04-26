#1) Countdown
def countdown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList
#print(countdown(5))

#2) Print and Return
def printReturn(arr):
    print(arr[0])
    return arr[1]
#print(printReturn([23,76]))

#3) First Plus Length
def firstPlus(arr):
    return arr[0] + len(arr)
algo3Array = [5,8,4,5,7]
#print(firstPlus(algo3Array))

#4) Values Greater than Second
def printGreaterSum(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] > arr[1]:
            sum += 1
    return sum
algo4Array = [1,3,5,7,9,13]
#print(printGreaterSum(algo4Array))

#5) Values Greater than Second, Generalized
def printGreaterSum2(arr):
    if len(arr) < 2:
        return "Array too short."
    sum = 0
    newArray = []
    for i in range(len(arr)):
        if arr[i] > arr[1]:
            sum += 1
            newArray.append(arr[i])
    print(sum)
    return newArray
algo5Array = [1,3,5,7,9,13]
#print(printGreaterSum2(algo5Array))

#6) This Length, That Value
def thisAndThat(num1, num2):
    if num1 == num2:
        return "Jinx!"
    newArray = []
    for i in range(num1):
        newArray.append(num2)
    return newArray
a = 2
b = 12
#print(thisAndThat(a, b))

#7) Fit the First Value
def goldilocks(arr):
    if(arr[0] > len(arr)):
        return "Too big!"
    elif(arr[0] < len(arr)):
        return "Too small!"
    else:
        return "Just right!"
algo7Array = [6,14,53,7,9,13]
#print(goldilocks(algo7Array))