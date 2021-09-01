#1) Setting and Swapping
def swapValues():
    myNumber = 42
    myName = 'Cameron'
    print(myNumber)
    print(myName)
    temp = myNumber
    myNumber = myName
    myName = temp
    print(myNumber)
    print(myName)
#swapValues()

#2) Print and Count
def printMultiplesOf5():
    sum = 0
    for i in range(5, 4096, 5):
        print(i)
        sum += 1
    print(sum)
#printMultiplesOf5()

#3) Print -52 to 1066
def printInt():
    for i in range(-52, 1067):
        print(i)
#printInt()

#4) Multiples of Six
def miultiplesOfSix():
    i = 6
    while i <= 60000:
        print(i)
        i += 6
#miultiplesOfSix()

#5) Don’t Worry, Be Happy
def beCheerful():
    for i in range(99):
        print("Number {}: Good morning!".format(i))
#beCheerful()

#6) Counting, the Dojo Way
def dojoCounting():
    for i in range(101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)
#dojoCounting()

#7) Multiples of Three – but Not All
def multiplesOfThree():
    for i in range(-300, 0, +3):
        if i == -6 or i == -3:
            continue
        else:
            print(i)
#multiplesOfThree()

#8) What Do You Know?
def printIncoming(input):
    print(input)
variable = "parameter"
#printIncoming(variable)

#9) Printing Integers with While
def printWithWhile():
    i = 2000
    while i <= 5280:
        print(i)
        i += 1
#printWithWhile()

#10) Whoa, That Sucker’s Huge...
def whoaBigNum():
    sum = 0
    for i in range(1, 300000, +2):
        sum += i
    return sum*2
#print(whoaBigNum())

#11) You Say It’s Your Birthday
def cakeDay(num1, num2):
    if num1 == 12 or num1 == 21:
        if num2 == 12 or num2 == 21:
            print("How did you know!?")
        else:
            print("Just another day....")
    else:
            print("Just another day....")
day = 12
month = 21
#cakeDay(day, month)

#12) Countdown by Fours
def countDown():
    i = 2016
    while i > 0:
        print(i)
        i -= 4
#countDown()

#13) Leap Year
def leapYear(input):
    if input % 4 == 0:
        if input % 100 == 0:
            if input % 400 == 0:
                print("A Special Kind of Leap Year!")
            else:
                print("Not a Leap Year.")
        else:
            print("Leap Year!")
    else:
        print("Not a Leap Year.")
year = 2000
#leapYear(year)

#14) Flexible Countdown
def flexibleCountdown(min, max, mult):
    for i in range(max, min, -mult):
        print(i)
flexibleCountdown(2,9,3)

#15) The Final Countdown
def finalCountdown(mult, min, max, exclude):
    while min <= max:
        if min % mult ==0:
            if min == exclude:
                min +=1
                continue
            print(min)
        min += 1
#finalCountdown(3,5,17,9)
