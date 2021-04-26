#1 - Biggie Size
def biggie(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = 'big'
    return arr
print(biggie([-1,3,5,-5]))

#2 - Previous Lengths
