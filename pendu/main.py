from PenduTools import *

print("Welcome to Pendu game !")
print("Current higher score {} - Try to beat it !!".format(getHigherScore()))
gameWinned = 0 

while True:
    print("!!! New Game !!!")
    wordToFind = getWordFromFile()  
    inputedLetter = ""  
    tmpWordState = "" 
    chance = 8  
    currentWordState = getWordFromSerialLetters(wordToFind, "")
    while not isWordCompleted(wordToFind, inputedLetter):
        print(currentWordState)
        if not chance:
            break
        print("Chance left: {}".format(chance))
        inputedLetter+= askNewLetter(inputedLetter)
        tmpWordState = getWordFromSerialLetters(wordToFind, inputedLetter)
        if tmpWordState == currentWordState:
            chance -= 1
        currentWordState = tmpWordState

    if isWordCompleted(wordToFind, inputedLetter):
        print("Congratulations !! You find the word \"{}\" :)".format(wordToFind))
        gameWinned += 1
    else:
        print("It's lost :'(")
        print("The expected word was \"{}\"".format(wordToFind))
    print("Your have a score of {} - Higher score {}".format(gameWinned, getHigherScore()))
    if gameWinned > getHigherScore():
        saveHigherScore(gameWinned)
    wantToContinue = input("Do you want to Continue ? (Y/n): ")
    if len(wantToContinue) != 0 and wantToContinue[0].lower() == "n":
        break

print("Goodbye")
