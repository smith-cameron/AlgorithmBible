import platform
print(platform.python_version())
#1 - Array: Shuffle******
#TESTING !@!#************************************************

#2 - Array: Remove Range******
def remove(input, idx):
    output = []
    if idx < 0:
        for i in range(1,len(input)):
            output.append(input[i])
        return output
    if idx > len(input):
        for i in range(len(input)-1):
            output.append(input[i])
        return output
    for i in range(len(input)):
        if i != idx:
            output.append(input[i])
    return output

def removeRange(input, idx1, idx2):
    # for i in range(idx1, idx2):
    #     input = remove(input,i)
    #     print(input)
    # return input
    for i in range(idx1, len(input)):
        if i <= idx2:
            input = remove(input,i)
        continue
    return input
#print(removeRange([20,30,40,50,60,70],2,4))
#****** shift/skip problem.

#3 - Intermediate Sums
def intSums(input):
    sum = 0
    for i in range(len(input)):
        sum += input[i]
        print(sum)
        print(input)
        if i > 1 and i % 9 == 0:
            input.append(sum)
            for i in range(len(input)-1, i,  -1):
                temp = input[i]
                input[i] = input[i-1]
                input[i-1] = temp
            sum = 0
        if i == len(input)-2:
            input.append(sum)

    return input
#print(intSums([1,2,1,2,1,2,1,2,1,2,1,2,1,2]))

#4 - Double Trouble
def doubleTrouble(input):
    newList = []
    for i in range(len(input)):
        newList.append(input[i])
        newList.append(input[i])
    return newList
#print(doubleTrouble([4, "ulysses", 42, False]))

#5 - Zip It******
def zipIt(input1, input2):
    newList = []
    len(input1)
    len(input2)
    for i in range(len(input1)):
        newList.append(input1[i])
        newList.append(input2[i])
    return newList
#print(zipIt([1,2,3],[4,5,6,7,8]))

def zipIt2(input1, input2):
    return input1
