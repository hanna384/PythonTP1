import random


random.seed()

__path_score = "./pendu/score"


def getWordFromFile(path="./pendu/mots.txt"):
    listWords = []
    for word in open(path, 'r'):  
        listWords.append(word.strip())
    return listWords[random.randint(0, len(listWords) - 1)]


def getWordFromSerialLetters(originalWord, lettersSerie):
    finalWord = ""
    for originalLetter in originalWord:
        if originalLetter in lettersSerie:
            finalWord += originalLetter
        else:
            finalWord += "_"
    return finalWord


def isWordCompleted(originalWord, lettersSerie):
    return "_" not in getWordFromSerialLetters(originalWord, lettersSerie)


def askNewLetter(letterSerie):
    newLetter = ""  
    while True:
        newLetter = lettreSaisie.get()
        newLetter.isalpha()
        if len(newLetter) > 0:
            newLetter = newLetter[0]
        if newLetter in letterSerie:
            print("You have already tried this letter !")
            newLetter = ""  
        if newLetter.isalpha():
            return newLetter


def getHigherScore():
    scoreFile = open(__path_score, "r+")
    return int(scoreFile.read())


def saveHigherScore(score):
    scoreFile = open(__path_score, "w")
    scoreFile.write(str(score))
    scoreFile.close()
