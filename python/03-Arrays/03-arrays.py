#1 - Array: Remove Negatives
def removeNegatives(input):
    for i in range(len(input)-1):
        if input[i] < 0:
            currentValue = input[i]
            for x in range(currentValue, len(input)-1):
                temp = input[x]
                input[x] = input[x+1]
                input[x+1] = temp
            input.pop()
    return input
print(removeNegatives([2,-1,3,-14,4]))