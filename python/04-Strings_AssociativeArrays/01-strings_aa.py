#1 - Remove Blanks
def removeBlanks(input):
    split = input.split(" ")
    return "".join(split)
#print(removeBlanks(" Pl ayTha tF u nkyM usi c "))

#2 - String: Get Digits
def getDigits(input):
    characters = []
    for i in range(2, len(input), +2):
        characters.append(input[i])
    output = "".join(characters)
    return output
#print(getDigits("0s1a3y5w7h9a2t4?6!8?0"))

#3 - Acronyms
def acronyms(input):
    sentance = input.split(" ")
    newStringList = []
    for string in range(len(sentance)):
        word = sentance[string]
        for i in range(len(word)):
            if i == 0:
                newStringList.append(word[i].capitalize())
    output = "".join(newStringList)
    return output
#print(acronyms("Live from New York, it's Saturday Night!"))

#4 - Count Non-Spaces
def nonSpaces(input):
    count = 0
    for i in range(0,len(input),+1):
        if input[i] != " ":
            count +=1
    return count
#print(nonSpaces("Honey pie, you are driving me crazy"))

#5 - Remove Shorter Strings ******
def removeShorts(list, boundary):
    i = 0
    while i < len(list)-1:
        if len(list[i]) < boundary:
            x = i
            while x < len(list)-1:
                temp = list[x]
                list[x] = list[x+1]
                list[x+1] = temp
                x += 1
            i+= 1
            list.pop()
        if len(list[0]) < boundary:
            x = 0
            while x < len(list)-1:
                temp = list[x]
                list[x] = list[x+1]
                list[x+1] = temp
                x += 1
            i+= 1
            list.pop()
    i += 1
    return list
# ****** if boundary is <= 4 the while loop never terminates... or starts. code just runs. if 5 or higher it works except for list[3] "k," ges skipped.
#print(removeShorts(["Live","f","New","k,","e","Saturday","Night!"], 5))

#6 - String: Reverse
def reverse(input):
    char = []
    for i in range(len(input)):
        char.append(input[i])
    for i in range(len(char)/2):
        temp = char[i]
        char[i] = char[len(char)-1-i]
        char[len(char)-1-i] = temp
    output = "".join(char)
    return output
#print(reverse("creature"))

#7 - Remove Even-Length Strings
def removeEvenStr(input):
    return input
print(removeEvenStr(["Nope!","Its","Kris","starting","with","K!","(instead","of","Chris","with", "C)","."]))