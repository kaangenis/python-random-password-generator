import random

numbersList = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1]
charList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upperList = []
symbolsList = ["!", "-", "^", "+", "-", "&", "/", "+", "?", "_", "-", "*","!", "+", "^", "+", "+", "&", "/", "-", "?", "_", "-", "*","+","-"]

easyList = []
regularList = []
expertList = []


for a in charList:
    x = a.upper()
    upperList.append(x)


def pickNumber():
    random.shuffle(numbersList)
    return random.choice(numbersList)

def pickChar():
    random.shuffle(charList)
    return random.choice(charList)

def pickUpper():
    random.shuffle(upperList)
    return random.choice(upperList)

def pickSymbol():
    random.shuffle(symbolsList)
    return random.choice(symbolsList)

pickList = [(random.choice(numbersList)), (random.choice(charList)), (random.choice(upperList)), (random.choice(symbolsList))]


def easyPass(a, b):
    firstList = []
    easyList.clear()

    easyChar = 0
    while easyChar != a:
        easyList.append(pickChar())
        easyChar += 1

    easyNumber = 0
    while easyNumber != b:
        easyList.append(pickNumber())
        easyNumber += 1
    
    random.shuffle(easyList)

    getEasy = random.choices(easyList, k = a)

    firstList.append(getEasy)

    myString = ' '
    for e in getEasy:
        myString += '' + str(e)

    print('Your Easy Password is: ', myString)



def regularPass(a,b,c):
    secondList = []
    regularList.clear()

    regularChar = 0
    while regularChar != a:
        regularList.append(pickChar())
        regularChar += 1

    regularNumber = 0
    while regularNumber != b:
        regularList.append(pickNumber())
        regularNumber += 1

    regularUpper = 0
    while regularUpper != c:
        regularList.append(pickUpper())
        regularUpper += 1

    random.shuffle(regularList)

    getRegular = random.choices(regularList, k = c)
    secondList.append(getRegular)

    myString = ' '
    for r in getRegular:
        myString += '' + str(r)

    print('Your Regular Password is: ', myString)



def expertPass(a,b,c,d):
    thirdList = []
    expertList.clear()

    expertChar = 0
    while expertChar != a:
        expertList.append(pickChar())
        expertChar += 1

    expertNumber = 0
    while expertNumber != b:
        expertList.append(pickNumber())
        expertNumber += 1

    expertUpper = 0
    while expertUpper != c:
        expertList.append(pickUpper())
        expertUpper += 1
    
    expertSymbol = 0
    while expertSymbol != d:
        expertList.append(pickSymbol())
        expertSymbol += 1

    random.shuffle(expertList)

    getExpert = random.choices(expertList, k = d)
    thirdList.append(getExpert)

    myString = ' '
    for t in getExpert:
        myString += '' + str(t)

    print('Your Expert Password is: ', myString)

        
appRun = True
while appRun == True:

    print("###########################################################################################")
    print("Welcome to Password Generator")
    print("Choice the password strong level you want")
    print("1-) Easy (Includes letters and numbers)")
    print("2-) Regular (Includes upper and regular letters, numbers)")
    print("3-) Expert (Includes upper and regular letters, numbers and symbols)")
    print("###########################################################################################")
    menuPick = int(input(" => "))

    if menuPick == 1:
        charENumber = int(input('How many characters do you want in your password? \n =>  '))
        easyPass(charENumber, charENumber)
    elif menuPick == 2:
        charRNumber = int(input('How many characters do you want in your password? \n =>  '))
        regularPass(charRNumber, charRNumber, charRNumber)
    elif menuPick == 3:
        charXNumber = int(input('How many characters do you want in your password? \n =>  '))
        expertPass(charXNumber, charXNumber, charXNumber, charXNumber)
    elif menuPick == 4:
        appRun = False
    else:
        print("Invalid value, try again")