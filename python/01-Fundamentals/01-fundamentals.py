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