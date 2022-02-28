import json


words_lol = []

with open("words.txt", 'r') as fyle:
    for line in fyle:
        words_lol.append(line.replace('\n', ''))

print(words_lol)

words_but_five = []

for word in words_lol:
    if (len(word) == 5):
        words_but_five.append(word.lower())

print(words_but_five)

words = words_but_five

wordGuessed = False
tries = 6



invalidLetters = []
yellowLetters = []
greenLetters = {}

filteredWords = []

def filterWords (prevWord, yL, gL, iL):
    firstPassWords = []
    for word in words:
        wordPossibles = []
        for letter in gL:
            if (word[gL[letter]] == letter):
                wordPossibles.append(True)
            else:
                wordPossibles.append(False)
        if (False not in wordPossibles):
            firstPassWords.append(word)
    #print(firstPassWords)
    secondPassWords = []
    if (len(yL) != 0):
        for word in firstPassWords:
            wordPossible = False
            for letter in yL:
                if (letter in word):
                    wordPossible = True
                if (letter not in word):
                    wordPossible = False
            if (wordPossible == True):
                secondPassWords.append(word)
    #print(secondPassWords)
    thirdPassWords = []
    #print(iL)
    if (len(secondPassWords) == 0):
        secondPassWords = firstPassWords
    for word in secondPassWords:
        for letter in iL:
            if (letter not in word):
                thirdPassWords.append(word)

            if (letter in word):
                break

    betterReturn = []

    for word in thirdPassWords:
        if (word not in betterReturn):
            if (word != previousWord and word not in filteredWords):
                betterReturn.append(word)
    #print(betterReturn)
    return(betterReturn)

def score (wordlist):
    letterScore = {}
    wordScore = {}

    for word in wordlist:
        for letter in word:
            if letter not in letterScore:
                letterScore[letter] = 1
            else:
                letterScore[letter] += 1

    for word in wordlist:
        indWordScore = 0
        for letter in word:
            indWordScore += letterScore[letter]
        wordScore[word] = indWordScore

    sortWordScore = dict(sorted(wordScore.items(),key= lambda x:x[1]))
    return(list(sortWordScore)[-1])

print(score(words))
while (wordGuessed == False and tries > 0):
    while True:
        wordleGuess = input("Input Word Guess: ")
        if (wordleGuess != "filter"):
            break
        else:
            filteredWords.append((score(filterWords(previousWord, yellowLetters, greenLetters, invalidLetters)))
)
            print(score(filterWords(previousWord, yellowLetters, greenLetters, invalidLetters)))

    previousWord = wordleGuess
    result = input("Input guess result (g = correct place correct letter, y = incorrect place correct letter, b = incorrect place & letter): ")\

    for i in range (0, len(previousWord)):
        if (result[i] == 'b'):
            if (result[i] not in invalidLetters):
                invalidLetters.append(previousWord[i])

        elif (result[i] == 'y'):
            if (result[i] not in yellowLetters):
                yellowLetters.append(previousWord[i])

        elif (result[i] == 'g'):
            if (result[i] not in greenLetters):
                greenLetters[previousWord[i]] = i

        else:
            print("Improper input")
    print("Possible next words:\n")
    print(filterWords(previousWord, yellowLetters, greenLetters, invalidLetters))

    print("Reccommended next word: " + score(filterWords(previousWord, yellowLetters, greenLetters, invalidLetters)))

    tries -= 1
