#1 - Array: Remove Negatives ******
def removeNegatives(input):
    for i in range(len(input)-1):
        print(len(input)-1)
        print(input)
        if input[i] < 0: #IndexError: list index out of range
            currentValue = i
            for x in range(currentValue, len(input)-1):
                temp = input[x]
                input[x] = input[x+1]
                input[x+1] = temp
            input.pop()
    return input
#print(removeNegatives([2,-1,3,-14,4]))
#****** As the list shrinks the for loop falls out of range.

#2 - Array: Second-to-Last
def secondLast(list):
    if len(list) < 2:
        return None
    else:
        return list[len(list)-2]
#print(secondLast([42,True,4,"Kate",7]))

#3 - Array: Second-Largest
def secondLargest(list):
    max = list[0]
    lastMax = 0
    if len(list) < 2:
        return None
    for i in range(len(list)):
        if list[i] > max:
            lastMax = max
            max = list[i]
        if list[i] > lastMax and list[i] < max:
            lastMax = list[i]
    return lastMax
#print(secondLargest([4,12,1,14,3,7]))

#4 - Array: Nth-to-Last
def nThLast(list, index):
    count = 1
    if len(list) < 2:
        return None
    for i in range(len(list)-1,0,-1):
        if count == index:
            return list[i]
        else:
            count += 1
#print(nThLast([5,2,3,6,4,9,7],3))

#5 - Array: Nth-Largest
def nThLargest(list, N):
    #if the list has less elements than the boundary value return null
    if len(list) < N:
        return None
    #return the Nth-largest element
print(nThLargest([5,2,3,6,4,9,7],3))