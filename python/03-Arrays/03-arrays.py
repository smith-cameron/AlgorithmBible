#1 - Array: Remove Negatives ******
def removeNegatives(input):
    # i = 0
    count = 0
    for i in range (len(input)):
        if input[i] < 0:
            # print(input[i])
            for x in range(i, len(input)-1):
                temp = input[x]
                input[x] = input[x+1]
                input[x+1] = temp
            input.pop()
            count += 1
            #i -=3

        i += 1
    # print("{} negatives".format(count))

    return input
#****** When input[i] is negative the function shifts it to the end(8-11). when it returns to line five it iterates +1 which skips the value shifted into the previous index

#print(removeNegatives([2,-1,0]))   #works 1
#print(removeNegatives([2,-1,0,-3]))   #works 2
#print(removeNegatives([2,0,4,-3]))  #works4
#print(removeNegatives([2,-1,0,-4,-3])) #leaves the -3
print(removeNegatives([2,-1,-4,0,-3])) #leaves the -4
#print(removeNegatives([2,-1,4,0,-3]))   #works 3

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

#5 - Array: Nth-Largest ******
def nThLargest(list, N):
    if len(list) < N:
        return None
    #return the Nth-largest element
#print(nThLargest([5,2,3,6,4,9,7],3))

#6 - Credit Card Validation
def isCreditCardValid(list):
    last = list[len(list)-1]
    list.pop()
    sum = 0
    for i in range(len(list)-1, 0, -2):
        list[i] *= 2
        if list[i] > 9:
            list[i] -= 9
    for i in range(len(list)):
        sum += list[i]
    sum += last
    return sum
#print(isCreditCardValid([5,2,2,8,2]))