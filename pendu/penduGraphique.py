from tkinter import Tk, Label, Button, PhotoImage, Canvas

myWindow = Tk()
myWindow.title('Le Pendu')
myWindow.geometry('700x500')




photo = PhotoImage(file = "pendu/Images/bonhomme8.gif")
Largeur = photo.height() 
Hauteur = photo.width()
Canevas = Canvas(myWindow, width = Largeur, height =Hauteur)
item = Canevas.create_image(0,0 , anchor ='nw' , image = photo)
Canevas.pack(side='right', expand=True)



Canevas.delete("all")
photo = PhotoImage(file = "pendu/Images/bonhomme" +"7" +".gif")
Largeur = photo.height() 
Hauteur = photo.width()
Canevas = Canvas(myWindow, width = Largeur, height =Hauteur)
item = Canevas.create_image(0,0 , anchor ='nw' , image = photo)
Canevas.pack(side='right', expand=True)



buttonQuit = Button (myWindow, text="Proposer", command = "")
buttonQuit.pack(side='left')



    
myWindow.mainloop()