letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

typeOfAction = input("\nВыберите что вы хотите сделать\n 1. Зашифровать \n 2. Расшифровать \n Впишите 1 либо 2: ")
wordToCipher = input("\nВведите слово для шифрования: ")
keyWord = input("\nВведите ключ для шифрования: ")

wordToCipherList = list(wordToCipher)
keyWordList = list(keyWord)

numbersOfLettersCipher = []
numbersOfKeyWord = []

resultOfSum = []
cipheredWord = []

if len(keyWordList) < len(wordToCipherList):
    for n in range(len(wordToCipherList)):
        keyWordList.append(keyWordList[n])

print(wordToCipherList, keyWordList)

for indexWord, letterWord in enumerate(wordToCipherList) :
    for indexKey, letterKey in enumerate(letters) :
        if letterWord == letterKey:
            numbersOfLettersCipher.append(indexKey)

for indexWord, letterWord in enumerate(keyWordList) :
    for indexKey, letterKey in enumerate(letters) :
        if letterWord == letterKey:
            numbersOfKeyWord.append(indexKey)

for i in range(len(numbersOfLettersCipher)):
    numberInWord = numbersOfLettersCipher[i]
    numberInKeyWord = numbersOfKeyWord[i]

    if numberInWord + numberInKeyWord <= 25:
        resultOfSum.append(numberInWord + numberInKeyWord)
    else:
        resultOfSum.append((numberInWord + numberInKeyWord) - 26)

for n in range(len(resultOfSum)):
    cipheredWord.append(letters[resultOfSum[n]])

print(''.join(cipheredWord))