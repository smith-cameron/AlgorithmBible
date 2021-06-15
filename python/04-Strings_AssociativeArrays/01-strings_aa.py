#1 - Remove Blanks
def removeBlanks(input):
    split = input.split(" ")
    return "".join(split)
#print(removeBlanks(" Pl ayTha tF u nkyM usi c "))

#2 - String: Get Digits
def getDigits(input):
    characters = []
    for i in range(2, len(input), +2):
        print(i)
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

#5 - Remove Shorter Strings
def stringLength(list, boundary):
    #iterate though string list
    i = 0
    while i < len(list)-1:
        if len(list[i]) < boundary:
            x = i
            while x < len(list)-1:
                temp = list[x]
                list[x] = list[x+1]
                list[x+1] = temp
                print(list)
                x += 1
            i+= 1
            list.pop()
        if len(list[0]) < boundary:
            x = 0
            while x < len(list)-1:
                temp = list[x]
                list[x] = list[x+1]
                list[x+1] = temp
                print(list)
                x += 1
            i+= 1
            list.pop()
    i += 1
    return list
print(stringLength(["Live","f","New","k,","e","Saturday","Night!"], 2))