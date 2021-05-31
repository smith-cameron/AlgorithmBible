#1 - Array: Min to Front
def minFront(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
            idx = i
    for i in range(idx, 0, -1) :
        temp = list[i]
        list[i] = list[i-1]
        list[i-1] = temp
    return list
#myList = [4,2,1,3,5,6]
#print(minFront(myList))

#2 - Array: Reverse
def reverse(list):
    for i in range(len(list)/2):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list
#print(reverse(myList))

#3 - Array: Rotate
def rotate(list, shift):
    for i in range(shift):
        temp = list[len(list)-1]
        for i in range(len(list)-1,0,-1):
            list[i] = list[i-1]
        list[0] = temp
    return list
aList = [1,2,3,4,5,6,7]
offset = 3
print(rotate(aList,offset))