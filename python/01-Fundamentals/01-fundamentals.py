#Set myNumber to 42. Set myName to your name. Now swap myNumber into myName & vice versa.
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

#Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.
def printMultiplesOf5():
    sum = 0
    for i in range(5, 4096, 5):
        print(i)
        sum += 1
    print(sum)
#printMultiplesOf5()

#Print integers from -52 to 1066 using a FOR loop.
def printInt():
    for i in range(-52, 1067):
        print(i)
#printInt()

#Print multiples of 6 up to 60,000, using a WHILE.
def miultiplesOfSix():
    i = 6
    while i <= 60000:
        print(i)
        i += 6
#miultiplesOfSix()

#Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.
def beCheerful():
    for i in range(99):
        print("Number {}: Good morning!".format(i))
#beCheerful()

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
def dojoCounting():
    for i in range(101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)
#dojoCounting()

#Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6
def multiplesOfThree():
    for i in range(-300, 0, +3):
        if i == -6 or i == -3:
            continue
        else:
            print(i)
#multiplesOfThree()

#Your function will be given an input parameter incoming. Please console.log this value.
def printIncoming(input):
    print(input)
variable = "parameter"
#printIncoming(variable)

#Print integers from 2000 to 5280, using a WHILE.
def printWithWhile():
    i = 2000
    while i <= 5280:
        print(i)
        i += 1
#printWithWhile()

#Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?
def whoaBigNum():
    sum = 0
    for i in range(1, 300000, +2):
        sum += i
    return sum*2
#print(whoaBigNum())

#If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day...."
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

#Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.
def countDown():
    i = 2016
    while i > 0:
        print(i)
        i -= 4
#countDown()

#Write a function that determines whether a given year is a leap year. If a year is divisible by four, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.
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

# given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).
def flexibleCountdown(min, max, mult):
    for i in range(max, min, -mult):
        print(i)
#flexibleCountdown(2,9,3)

# Given 4 parameters param1param2param3param4 print the multiples of param1 starting at param2 and extending to param3 One exception if a multiple is equal to param4, then skip it. Do this using a WHILE. Given 3,5,17,9 print 6,12,15 which are all of the multiples of 3 between 5 and 17, and excluding the value 9
def finalCountdown(mult, min, max, exclude):
    while min <= max:
        if min % mult ==0:
            if min == exclude:
                min +=1
                continue
            print(min)
        min += 1
#finalCountdown(3,5,17,9)

