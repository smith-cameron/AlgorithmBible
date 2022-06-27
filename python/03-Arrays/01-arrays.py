#1 - Array: Push Front
def pushFront(input, num):
    output = [num] + input
    return output
# print(pushFront([1,2,3,4],8))

#2 - Array: Pop Front
def popFront(input):
    # print(input)
    for i in range(len(input)-1):
        temp = input[i]
        input[i] = input[i+1]
        input[i+1] = temp
    # print(input)
    input.pop()
    return input
# print(popFront([1,2,3,4]))

#3 - Array: Insert At
def insert(input, idx, num):
    # print(input)
    output = [num] + input
    print(output)
    for i in range(output[idx]):
        temp = output[i]
        output[i] = output[i+1]
        output[i+1] = temp
    return output
# print(insert([1,2,3,4],2,5))

#3 - Array: Insert At (working in place) *NOT FINISHED*
def insert(input, idx, num):
    print(input)
    for i in range(idx, len(input)):
        print("idx: ",i)
        print("value: ",input[i])
    return input
print(insert([1,2,3,4],2,5))

#4 - Array: Remove At
def remove(input, idx):
    for i in range(len(input)-1):
        if i == idx:
            temp = input[i]
            input[i] = input[i+1]
            input[i+1] = temp
    return len(input)-1
# print(remove([1,2,3,4], 2))

#5 - Array: Swap Pairs
def swapPairs(input):
    for i in range(0, len(input)-1, +2):
        temp = input[i]
        input[i] = input[i+1]
        input[i+1] = temp
    return input
#print(swapPairs(["Brendan",True,42,False]))

#6 - Array: Remove Duplicates
def removeDuplicates(input):
    newList = []
    for i in range(len(input)):
        # print(input[i])
        if input[i] != input[i-1]:
            print()
            newList.append(input[i])
        else:
            print(input[i])
    return newList
# print(removeDuplicates([1,1,2,2,3,4,4,5,6,7,7,8,9,9]))

def remove(input, idx):
    size = len(input)
    if idx <= 0:
        return [input[i] for i in range(1,size)]
    if idx >= size:
        return [input[i] for i in range(size-1)]
    return [input[i] for i in range(size) if i != idx]

#print(remove([1,2,3,4], 0))
