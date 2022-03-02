import json


words_lol = []

with open("words.txt", 'r') as fyle:
    for line in fyle:
        words_lol.append(line.replace('\n', ''))

#print(words_lol)

words_but_five = []

for word in words_lol:
    if (len(word) == 5):
        words_but_five.append(word.lower())

#print(words_but_five)

words = words_but_five

wordGuessed = False
tries = 6



invalidLetters = []
yellowLetters = {}
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
        """
        for word in firstPassWords:
            wordPossible = False
            for letter in yL:
                if (letter in word):
                    wordPossible = True
                if (letter not in word):
                    wordPossible = False
            if (wordPossible == True):
                secondPassWords.append(word)
        """

        for word in firstPassWords:
            wordPossibles = []
            ylnum = 0
            lenOfYL = 0
            for yl in yL:
                lenOfYL += len(yL[yl])
            for stupidYellowLetter in yL:
                for placer in yL[stupidYellowLetter]:
                    if (word[placer] == stupidYellowLetter):
                        ylnum += 1
                if (ylnum == lenOfYL):
                    for letter in yL:
                        for yl in yL[letter]:
                            if (word[yl] == letter):
                                wordPossibles.append(False)
                                break
                    if (False not in wordPossibles):
                        secondPassWords.append(word)

        for word in firstPassWords:
            shouldBeFiltered = []
            for bruhLetter in yL:
                for placeSingle in yL[bruhLetter]:
                    thisIsAGreenLetter = False
                    try:
                        if (word[placeSingle] == gL[bruhLetter]):
                            thisIsAGreenLetter = True
                    except:
                        pass

                    if (not thisIsAGreenLetter):
                        everyLetterInWord = []
                        for letter in word:
                            for bitch in yL:
                                if (bitch in word):
                                    everyLetterInWord.append(True)
                                else:
                                    everyLetterInWord.append(False)
                                for place in yL[bitch]:
                                    if (word[place] == bitch or (False in everyLetterInWord)):
                                        filteredWords.append(word)
 #   print(secondPassWords)
  #  print("^^^^")
    thirdPassWords = []
    #print(iL)
    if (len(secondPassWords) == 0):
#        print("AYO THIS SHIT EMPTY")
       # if (len(firstPassWords) == 0):
#            print("ayo this shit empty too")
        secondPassWords = firstPassWords
    for word in secondPassWords:
        addThisWord = True
        for stupidAssLetter in word:
            for thisIsAStupidAssInvalidLetter in iL:
                if (stupidAssLetter == thisIsAStupidAssInvalidLetter):
                    addThisWord = False
        if (addThisWord == True):
            thirdPassWords.append(word)

    betterReturn = []
#    print(thirdPassWords)
#    print("before the loop")
#    print(iL)
    #print(filteredWords)
    for word in thirdPassWords:
        if (word not in betterReturn):
            if (word != previousWord and word not in filteredWords):
#                print(iL)
                addThisWord = True
                for stupidAssLetter in word:
                    for thisIsAStupidAssInvalidLetter in iL:
                        if (stupidAssLetter == thisIsAStupidAssInvalidLetter):
                            addThisWord = False

                if (addThisWord == True):
                    betterReturn.append(word)
    print("Possible words: " + str(len(betterReturn)))

    if (len(betterReturn) < 10):
        print(betterReturn)
    return(betterReturn)

def score (wordlist, offset=0):
    letterScore = {'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8, 'q': 10, 'z': 10, "'": 1000, '.': 1000}
    wordScore = {}

    for word in wordlist:
        indWordScore = 0
        dupLetters = []
        dupCount = 0
        for letter in word:
            indWordScore += letterScore[letter]
            dupLetters.append(letter)
        for letter in dupLetters:
            for dup in dupLetters:
                if (dup == letter):
                    dupCount += 1
        if (dupCount > 1):
            for x in range (0, dupCount):
                indWordScore = indWordScore * indWordScore
        wordScore[word] = indWordScore

    sortWordScore = dict(sorted(wordScore.items(),key= lambda x:x[1]))
    #print(sortWordScore)
    return(list(sortWordScore)[0 + offset])

print("Suggested word: penis")
print("Reccommended next word: " + score(words))

prevSuggWord = score(words)
previousWord = ""
offed = 0
while (wordGuessed == False and tries > 0):
    while True:
        wordleGuess = input("Input Word Guess: ")
        if (wordleGuess != "filter"):
            break
        else:
            offed += 1
            filteredWords.append(prevSuggWord)
            if (tries != 6):
                print(score(filterWords(previousWord, yellowLetters, greenLetters, invalidLetters)))
            else:
                print(score(words, offed))

    previousWord = wordleGuess
    result = input("Input guess result (g = correct place correct letter, y = incorrect place correct letter, b = incorrect place & letter): ")

    if (result == 'ggggg'):
        print("Cool mode <:D")
        wordGuessed = True
        break
    else:
        for i in range (0, len(previousWord)):
            if (result[i] == 'b'):
                invalidLetters.append(previousWord[i])
                #print("I DID A FUCKING THING HOLLLYSHIT")

            elif (result[i] == 'y'):
                if (previousWord[i] not in yellowLetters):
                    yellowLetters[previousWord[i]] = i
                    yellowLetters[previousWord[i]] = [yellowLetters[previousWord[i]]]
                else:
                    yellowLetters[previousWord[i]].append(i)

                #print(yellowLetters)

            elif (result[i] == 'g'):
                greenLetters[previousWord[i]] = i

            else:
                print("Improper input")
    #print("Possible next words:\n")
    #print(filterWords(previousWord, yellowLetters, greenLetters, invalidLetters))
    #print(invalidLetters)
    print("Reccommended next word: " + score(filterWords(previousWord, yellowLetters, greenLetters, invalidLetters)))
    prevSuggWord = score(filterWords(previousWord, yellowLetters, greenLetters, invalidLetters))
    tries -= 1
