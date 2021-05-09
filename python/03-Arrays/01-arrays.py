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
    for i in range()
print(remove([1,2,3,4], 2))