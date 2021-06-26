#1 - Array: Push Front
def pushFront(input, num):
    output = [num] + input
    return output
#print(pushFront([1,2,3,4],8))

#2 - Array: Pop Front
def popFront(input):
    for i in range(len(input)-1):
        temp = input[i]
        input[i] = input[i+1]
        input[i+1] = temp
    input.pop()
    return input
#print(popFront([1,2,3,4]))

#3 - Array: Insert At
def insert(input, idx, num):
    output = [num] + input
    for i in range(output[idx]):
        temp = output[i]
        output[i] = output[i+1]
        output[i+1] = temp
    return output
#print(insert([1,2,3,4],2,5))

#4 - Array: Remove At
def remove(input, idx):
    for i in range(len(input)-1):
        if i == idx:
            temp = input[i]
            input[i] = input[i+1]
            input[i+1] = temp
    return input.pop()
#print(remove([1,2,3,4], 2))

#5 - Array: Swap Pairs
def swapPairs(input):
    for i in range(0, len(input)-1, +2):
        temp = input[i]
        input[i] = input[i+1]
        input[i+1] = temp
    return input
#print(swapPairs(["Brendan",True,42,False]))

#6 - Array: Remove Duplicates ***********
def removeDuplicates(input):
    # i = 0
    for i in range(len(input)) :
        if input[i] == input[i-1]:
            index = i
            for i in range(index, len(input)-1):
                temp = input[i]
                input[i] = input[i+1]
                input[i+1] = temp
            # print(input)
            # input.pop()
            #i+=1
        #i+=1
    return input
print(removeDuplicates([1,1,2,3,4,4,5,6,7,7,8,9]))
