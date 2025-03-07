letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

typeOfAction = input("\nВыберите что вы хотите сделать\n 1. Зашифровать \n 2. Расшифровать \n Впишите 1 либо 2: ")
wordToCipher = list(input("\nВведите слово для шифрования: "))
keyWord = list(input("\nВведите ключ для шифрования: "))

numbersOfLettersCipher = []
numbersOfKeyWord = []

cipheredWord = []

def makeKeyWordAndWordSameLength(wordToCipherList, keyWordList):
    newKeyWordList = []

    if len(keyWordList) < len(wordToCipherList):
        for j in range(len(wordToCipherList)):
            newKeyWordList.append(keyWordList[j % len(keyWordList)])

    return newKeyWordList

def replaceLettersToIndexes(wordList, letters):
    arrayWithNewIndexes = []

    for indexWord, letterWord in enumerate(wordList) :
        for indexKey, letterKey in enumerate(letters) :
            if letterWord == letterKey:
                arrayWithNewIndexes.append(indexKey)

    return arrayWithNewIndexes

def sumTheArrays(cipheredWordList, keyWordList, action):
    result = []

    for i in range(len(cipheredWordList)):
        numberInWord = cipheredWordList[i]
        numberInKeyWord = keyWordList[i]

        print(numberInWord, numberInKeyWord)

        if action == "1":
            if numberInWord + numberInKeyWord <= 25:
                result.append(numberInWord + numberInKeyWord)
            else:
                result.append((numberInWord + numberInKeyWord) - 26)
        elif action == "2":
            if numberInWord - numberInKeyWord >= 0:
                result.append(numberInWord - numberInKeyWord)
            else:
                result.append((numberInWord - numberInKeyWord + 26))

    return result

keyWordWithRightLength = makeKeyWordAndWordSameLength(wordToCipher, keyWord)
indexesCipherWord = replaceLettersToIndexes(wordToCipher, letters)
indexesKeyWord = replaceLettersToIndexes(keyWordWithRightLength, letters)
resultOfSum = sumTheArrays(indexesCipherWord, indexesKeyWord, typeOfAction)

for n in range(len(resultOfSum)):
    cipheredWord.append(letters[resultOfSum[n]])

print(''.join(cipheredWord))