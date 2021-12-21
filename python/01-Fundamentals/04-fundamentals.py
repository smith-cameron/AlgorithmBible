#1- Only Keep the Last Few
def decrementDirect(input, x):
    toRemove = len(input)-x
    len(input)- toRemove
    return input
print(decrementDirect([2,4,6,8,10], 3))