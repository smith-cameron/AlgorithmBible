#2.1 - Threes and Fives
def threesFives():
    sum = 0
    for i in range(100, 4000001):
        if i % 3 == 0 and i % 5 == 0:
            pass
            #print("{} is divisable by both 3 & 5 so does not qualify. Total is: {}".format(i, sum))
        if i % 3 == 0:
            sum += i
            #print("{} is divisable by 3. Added. New total: {}".format(i, sum))
        if i % 5 == 0:
            sum += i
            #print("{} is divisable by 5. Added. New total: {}".format(i, sum))
    return sum
#print("{} is the total sum.".format(threesFives()))

#2.2 - Threes and Fives
def betterThreesFives(start,end):
    sum = 0
    for i in range(start, end):
        if i % 3 == 0 and i % 5 == 0:
            pass
            #print("{} is divisable by both 3 & 5 so does not qualify. Total is: {}".format(i, sum))
        if i % 3 == 0:
            sum += i
            #print("{} is divisable by 3. Added. New total: {}".format(i, sum))
        if i % 5 == 0:
            sum += i
            #print("{} is divisable by 5. Added. New total: {}".format(i, sum))
    return sum
num1 = 49
num2 = 233
#print("{} is the total sum.".format(betterThreesFives(num1, num2)))

#3 - Generate Coin Change
def makingCents(input):




myCents = 78
print(makingCents(myCents))