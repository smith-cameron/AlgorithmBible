#1 - Sigma
def sigma(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum
#print(sigma(5))

#2 - Factorial
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
#print(factorial(5))

#3.1 - Star Art
def drawLeftStars(num):
    print("*"*num)
#drawLeftStars(25)

#3.2 - Star Art
def drawRightStars(num):
    if num > 74:
        return "{} Excedes character limit.".format(num)
    if num < 1:
        return "Please input a positive integer value of characters."
    return "|"+" "*(75-num)+"*"*num
#print(drawRightStars(285))

#3.3 - Star Art
def drawCenteredStars(num):
    if num > 73:
        print(num)
        return "Input excedes character limit."
    if num < 1:
        return "Please input a positive integer value of characters."
    outside = (75-num)/2
    return "|"+" "*outside+"*"*num+" "*outside+"|"
#print(drawCenteredStars(30))

#3.4 - Star Art
def starWars():
    xWing = ">o<"
    tieF = "|=|"
    yWing = ">-=D"
    print(xWing+"     "+tieF+"     "+yWing)
#starWars()

#4.1 - Character Art
def drawLeftChars(num,char):
    print(char*num)
#drawLeftChars(10, "X")

#4.2 - Character Art
def drawRightChars(num,char):
    if num > 74:
        return "{} Excedes character limit.".format(num)
    if num < 1:
        return "Please input a positive integer value of characters."
    return "|"+" "*(75-num)+(char*num)
#print(drawRightChars(20, "X"))

#4.3 - Character Art
def drawCenteredChars(num,char):
    if num > 73:
        return "{} Excedes character limit.".format(num)
    if num < 1:
        return "Please input a positive integer value of characters."
    boundary = (75-num)/2
    return "|"+" "*boundary+"*"*num+" "*boundary+"|"
#print(drawCenteredChars(45, "X"))