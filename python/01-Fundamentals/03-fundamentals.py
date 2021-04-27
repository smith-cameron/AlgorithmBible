#1 - Biggie Size
def biggie(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = 'big'
    return arr
#print(biggie([-1,3,5,-5]))

#2 - Previous Lengths
def prevLength(arr):
    for i in range(len(arr)-1,-1,-1):
        if i == 0:
            arr[i] = 0
            return arr
        arr[i] = len(arr[i-1])
    return arr
#print(prevLength(["I", "am", "the", "best"]))

#3 - Print Low, Return High
def minReturnMax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    print(min)
    return max
#print(minReturnMax([2,7,3,5,8,9,3]))

#4 - Add Seven to Most
def addSeven(arr):
    newArray = []
    for i in range(1,len(arr), +1):
        newArray.append(arr[i]+7)
    return newArray
#print(addSeven([1,2,3,4]))

#5 - Print One, Return Another
def secondToLast(arr):
    print(arr[len(arr)-2])
    odd = 0
    for i in range(len(arr)):
        if arr[i]% 2 != 0:
            odd = arr[i]
            return odd
#print(secondToLast([6,3,8,9,1,2,5,8]))

#6 - Reverse Array
def reverseArray(arr):
    for i in range(len(arr)/2):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr
#print(reverseArray([3,1,6,4,2,9]))

#7 - Double Vision
def doubleTrouble(arr):
    newArray = []
    for i in range(len(arr)):
        newArray.append(arr[i]*2)
    return newArray
#print(doubleTrouble([1,2,3]))

#8 - Outlook: Negative
def negatives(arr):
    newArray = []
    for i in range(len(arr)):
        if arr[i] < 0:
            newArray.append(arr[i])
        else:
            newArray.append(arr[i]*-1)
    return newArray
#print(negatives([1,-3,5]))

#9 - Count Positives
def countPositives(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            sum += 1
    arr[len(arr[i])] = sum
    return arr
#print(countPositives([-1,1,1,1]))

#10 - Always Hungry
def alwaysHungry(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == "food":
            print("mmmm... yummy.")
            count += 1
    if count == 0:
        print("I'm hungry!")
#alwaysHungry(["word", False, "another string", 34, "no", "blah"])

#11 - Evens and Odds
def evensAndOdds(arr):
    for i in range(len(arr)-2):
        if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
            print("That's odd!")
        if arr[i] % 2 == 0 and arr[i+1] % 2 == 0 and arr[i+2] % 2 == 0:
            print("Even more so!")
#evensAndOdds([1,3,9,4,5,6,7,8,9,2])

#12 - Swap Toward the Center
def swapInwards(arr):
    for i in range(0,len(arr)/2, +2):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr
#print(swapInwards([1,2,3,4,5,6]))

#13 - Increment the Seconds
def incrementOdds(arr):
    for i in range(len(arr)):
        if i % 2 != 0:
            arr[i] += 1
    return arr
#print(incrementOdds([1,2,3,4,5,6]))

#14 - Scale the Array
def scaleable(arr, num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr
print(scaleable([1,2,3,4,5,6], 2))