from tkinter import*
import threading
from random import *

Points = [0]
Time = [2.0]
Total = [0]
Mole1 = [0,0]
Mole2 = [0,0]


class App(Frame):
    def __init__(self, win):
        self.win=win
        super().__init__(self.win)
        self.grid()
        self.M = [[0 for j in range(5)]for i in range(5)]
        self.Sucelje()

    def OnClick(self,cordx,cordy):
        if cordx == Mole1[0] and cordy == Mole1[1]:
            Points[0] += 1
            Total[0] += 1
            if Time[0] >= 1:            
                Time[0] = Time[0] - 0.1
            self.lab1.config(text = 'Points : ' + str(Points[0]))
            self.lab2.config(text = f'Time to whack :  {Time[0]:.2f}  sec')
            self.lab3.config(text = f'W/M : {((Points[0]/Total[0])*100):.0f} %')
            self.M[Mole1[0]][Mole1[1]].config(image = HoleImg)
            Mole1[0] = -1
            Mole1[1] = -1
            
        elif cordx == Mole2[0] and cordy == Mole2[1]:
            Points[0] += 1
            Total[0] += 1
            if Time[0] >= 1:
                Time[0] = Time[0] - 0.1
            self.lab1.config(text = 'Points : ' + str(Points[0]))
            self.lab2.config(text = f'Time to whack :  {Time[0]:.2f}  sec')
            self.lab3.config(text = f'W/M : {((Points[0]/Total[0])*100):.0f} %')
            self.M[Mole2[0]][Mole2[1]].config(image = HoleImg)
            Mole2[0] = -1
            Mole2[1] = -1

            
        else:
            Time[0] = Time[0] + 0.1
            Total[0] += 1
            self.lab2.config(text = f'Time to whack :  {Time[0]:.2f}  sec')
            self.lab3.config(text = f'W/M : {((Points[0]/Total[0])*100):.0f} %')
          
        
    def Sucelje(self):
        w = 128
        h = 128
        for i in range(5):
            for j in range(5):
                self.but = Button(self, text='',width=w, height=h, command = lambda x=i,y=j: self.OnClick(x,y))
                self.but.grid(row = i+1, column = j+1)
                self.M[i][j] = self.but

        self.lab1 = Label(self,text = 'Points : 0', font = ('Arial',15))
        self.lab1.grid(row = 2, column = 6)

        self.lab3 = Label(self,text = 'W/M : 100%',  font = ('Arial',15))
        self.lab3.grid(row = 3, column = 6)

        self.lab2 = Label(self,text = 'Time to whack : 2.0 sec',  font = ('Arial',15))
        self.lab2.grid(row = 4, column = 6)



                              
Apl=App(Tk())
HoleImg = PhotoImage(file='NoAlaber.png')
MoleImg = PhotoImage(file = 'Alaber.png')
for i in range(5):
    for j in range(5):
        Apl.M[i][j].config(image = HoleImg)


def printit():
    Apl.M[Mole1[0]][Mole1[1]].config(image = HoleImg)
    Apl.M[Mole2[0]][Mole2[1]].config(image = HoleImg)    
    threading.Timer(Time[0], printit).start()
    Mole1[0] = randint(0,4)
    Mole1[1] = randint(0,4)
    Mole2[0] = randint(0,4)
    Mole2[1] = randint(0,4)
    while Mole1[0] == Mole2[0] and Mole1[1] == Mole2[1]:
        Mole2[0] = randint(0,4)
        Mole2[1] = randint(0,4)
        
    Apl.M[Mole1[0]][Mole1[1]].config(image = MoleImg)
    Apl.M[Mole2[0]][Mole2[1]].config(image = MoleImg)


    

printit()

Apl.mainloop()
