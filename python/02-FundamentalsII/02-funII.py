#2.1 - Threes and Fives
def threesFives():
    sum = 0
    for i in range(100, 4000001):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} is divisable by both 3 & 5 so does not qualify. Total is: {sum}")
            continue
        if i % 3 == 0:
            sum += i
            print(f"{i} is divisable by 3. Added. New total: {sum}")
        if i % 5 == 0:
            sum += i
            print(f"{i} is divisable by 5. Added. New total: {sum}")
    return sum
#print(f"{threesFives()} is the total sum.")

#2.2 - Threes and Fives
def betterThreesFives(start,end):
    sum = 0
    for i in range(start, end):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} is divisable by both 3 & 5 so does not qualify. Total is: {sum}")
            continue
        if i % 3 == 0:
            sum += i
            print(f"{i} is divisable by 3. Added. New total: {sum}")
        if i % 5 == 0:
            sum += i
            print(f"{i} is divisable by 5. Added. New total: {sum}")
    return sum
num1 = 49
num2 = 233
#print(f"{betterThreesFives(num1, num2)} is the total sum.")

#3.1-3.3 - Generate Coin Change
def makingCents(chg):
    if chg > 100:
        DL = chg/100
        print(f'Dollars: {DL}')
        chg -= (DL*100)
    if chg > 50:
        HD = chg/50
        print(f'Half-Dollar: {HD}')
        chg -= (HD*50)
    if chg > 25:
        Q = chg/25
        print(f'Quarters: {Q}')
        chg -= (Q*25)
    if chg > 10:
        D = chg/10
        print(f'Dimes: {D}')
        chg -= (D*10)
    if chg > 5:
        N = chg/5
        print(f'Nickles: {N}')
        chg -= (N*5)
    if chg > 1:
        P = chg/1
        print(f'Pennies: {P}')
        chg -= (P*1)
myCents = 297
#makingCents(myCents)

def coins(chg):
    dollars = 0
    halfDollars = 0
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    while chg > 0:
        while chg >= 100:
            chg -= 100
            dollars += 1
        while chg >= 50:
            chg -= 50
            halfDollars += 1
        while chg >= 25:
            chg -= 25
            quarters += 1
        while chg >= 10:
            chg -= 10
            dimes += 1
        while chg >= 5:
            chg -= 5
            nickles += 1
        while chg >= 1:
            chg -= 1
            pennies += 1
        return dollars, halfDollars, quarters, dimes, nickles, pennies

def coins2(coin):
    change=[]
    change.append(int(coin/25))
    change.append(int((coin%25)/10))
    change.append(int(((coin%25)%10)/5))
    change.append(int(((coin%25)%10)%5))
    return(change)

print(coins2(40))
#print(coins(myCents))

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
#print(messyMath(8))

#5 - Twelve-Bar Blues
def blues():
    for i in range(1, 13):
        print(i)
        print("chick, boom, chick")
#blues()

#6 - Fibonacci
def fibonacci(num):
    if num == 0:
        return 0
    if num == 2 or num == 1:
        return 1
    num1 = 0
    num2 = 1
    sum = 0
    for i in range(num-1):
        sum = num1 + num2
        num1 = num2
        num2 = sum
    return num2
fibNum = 6
#print(fibonacci(fibNum))

def rFibonacci(num):
    if num <= 2:
        return 1
    return rFibonacci(num - 1) + rFibonacci(num - 2)
#print(rFibonacci(fibNum))

#7 - Sum to One Digit
def sumToOne(num):
    num = [int(i) for i in str(num)]
    sum = 0
    if len(num) == 1:
        return num[0]
    for i in range(len(num)):
        sum += num[i]
    return sumToOne(sum)
#print(sumToOne(927))

#8 - Clock Hand Angles ******
def clockHandAngles(seconds):
    hourD = 0
    minD = 0
    secD = 0
    #for seconds input = 3600 return hourD = 30. minD = 0. secD = 0
    #for seconds input = 119730 return hourD = 277.745. minD = 93. secD = 180
    print(f"Hour hand: {hourD} degs. Minute hand: {minD} degs. Second hand: {secD} degs.")
#clockHandAngles(3600)

#9 - Is Prime
def isPrime(num):
    if num % 2 == 0 or num % 3 == 0:
        return "Nope, not a prime #!"
    return "Thats prime!"
#print(isPrime(11))

#10 - Rockin’ the Dojo Sweatshirt
def sweatshirtPricing(num):
    print(f"{num} sweatshirts")
    cost = 0
    if num >= 4:
        cost = (num * 20) - (60 * .35)
        print(f"discount is: ${(60 * .35)}")
    elif num == 3:
        cost = (num * 20) - (60 * .19)
        print(f"discount is: ${(60 * .19)}")
    elif num == 2:
        cost = (num * 20) - (40 * .09)
        print(f"discount is: ${(40 * .09)}")
    else:
        cost = (num * 20)
    return round(cost, 0)
sweatshirts = 5
#print(f"Total Bill: ${sweatshirtPricing(sweatshirts)}")

#11 - Clock Hand Angles, Revisited ******
