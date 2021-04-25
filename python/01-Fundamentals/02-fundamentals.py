#1) Countdown
def countdown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList
print(countdown(5))