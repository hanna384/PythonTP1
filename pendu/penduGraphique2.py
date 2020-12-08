# le 08 décembre 2020
# programme écrit par Hanna Albala

# ToDo : recuperer la lettre entrée par l'user

#from tkinter import Tk, Label, Button, PhotoImage, Canvas
from tkinter import *

from PenduTools import *


def changeImage(nbChanceLeft):
    Canevas.delete("all")
    photo = PhotoImage(file = "pendu/Images/bonhomme" + chance +".gif")
    Largeur = photo.height() 
    Hauteur = photo.width()
    Canevas = Canvas(myWindow, width = Largeur, height =Hauteur)
    item = Canevas.create_image(0,0 , anchor ='nw' , image = photo)
    Canevas.pack(side='right', expand=True)

def Proposer(): 
    gameWinned = 0

    while True:
        wordToFind = getWordFromFile()  
        inputedLetter = ""  
        tmpWordState = ""  
        chance = 8 
        currentWordState = getWordFromSerialLetters(wordToFind, "")
        while not isWordCompleted(wordToFind, inputedLetter):
            motvariable = currentWordState
            if not chance:
                break
            print("Chance left: {}".format(chance))
            inputedLetter+= askNewLetter(inputedLetter)
            tmpWordState = getWordFromSerialLetters(wordToFind, inputedLetter)
            if tmpWordState == currentWordState:
                chance -= 1
                changeImage(chance)
            currentWordState = tmpWordState

        if isWordCompleted(wordToFind, inputedLetter):
            felicitation = Label(myWindow, text = "Félicitation ! vous avez trouvé le mot" + wordToFind)
            motAffiche.pack(side='bottom')
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


myWindow = Tk()
myWindow.title('Jeu du Pendu')
myWindow.geometry('800x500')



messageAcceuil = Label(myWindow, text = "Bienvenu au jeu du pendu !", fg = 'blue')
messageAcceuil.pack(side='top')

LabelEntryLettre = Label(myWindow, text = "Proposer une lettre")
LabelEntryLettre.pack(side='left')

letteSaisie = Entry(myWindow)
letteSaisie.focus_set()
letteSaisie.pack(side='left', padx = 5, pady = 5)

buttonQuit = Button (myWindow, text="Proposer", command = Proposer)
buttonQuit.pack(side='left')



photo = PhotoImage(file = "pendu/Images/bonhomme8.gif")
Largeur = photo.height() 
Hauteur = photo.width()
Canevas = Canvas(myWindow, width = Largeur, height =Hauteur)
item = Canevas.create_image(0,0 , anchor ='nw' , image = photo)
Canevas.pack(side='right', expand=True)


motvariable = StringVar()
motvariable = "_ _ _"
motAffiche = Label(myWindow, text = motvariable )
motAffiche.pack(side='bottom')






myWindow.mainloop()





