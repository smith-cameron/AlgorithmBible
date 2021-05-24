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

#3.1-3.3 - Generate Coin Change
def makingCents(chg):
    if chg > 100:
        DL = chg/100
        print('Dollars: {}'.format(DL))
        chg -= (DL*100)
    if chg > 50:
        HD = chg/50
        print('Half-Dollar: {}'.format(HD))
        chg -= (HD*50)
    if chg > 25:
        Q = chg/25
        print('Quarters: {}'.format(Q))
        chg -= (Q*25)
    if chg > 10:
        D = chg/10
        print('Dimes: {}'.format(D))
        chg -= (D*10)
    if chg > 5:
        N = chg/5
        print('Nickles: {}'.format(N))
        chg -= (N*5)
    if chg > 1:
        P = chg/1
        print('Pennies: {}'.format(P))
        chg -= (P*1)
myCents = 193
#makingCents(myCents)

#4 - Messy Math Mashup
def messyMath(num):
    sum = 0
    for i in range(num+1):
        if i % 3 == 0:
            continue
        if i % 7 == 0:
            sum += (i*2)
        else:
            sum += i
        if i == (num % 3 == 0):
            return -1
    return sum
print(messyMath(8))