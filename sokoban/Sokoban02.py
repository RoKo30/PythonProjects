from turtle import*

colormode(255)
global Lvlnum
Lvlnum = 0

dat = open('Levels.txt','r')
LevelList00 = dat.read()
LevelList01 = LevelList00.split('Level')
tracer(False)

#lenght of one unit
l=50

#box
def box(l):
    for i in range(4):
        fd(l)
        rt(90)

#Drawings
def wall(l):
    box(l)
    rt(45)
    fd((2*(l)**2)**(1/2))
    rt(135)
    for i in range(2):
        fd(l)
        rt(90)
        
def crate(l):
    wall(l)
    fd(l)
    rt(135)
    fd((2*(l)**2)**(1/2))
    rt(135)
    fd(l)
    rt(90)


#Matrix formated print
def matprint(a,b,M):
    for i in range(a):
        for j in range(b):
            print(M[i][j],end = ' ')
        print()
        
#polje
class Cell:
    def __init__(self,Type = ' '):
        self.ty = Type

    def __str__(self):
        return '{}'.format(self.ty)
        

    def draw(self):
        if self.ty == '#':
            fillcolor(50,50,50)
            pd()
            begin_fill()
            wall(l)
            end_fill()    
        if self.ty == ' ':
            fillcolor(255,255,255)
            pd()
            begin_fill()
            box(l)
            end_fill()
        if self.ty == '.':
            fillcolor('yellow')
            pd()
            begin_fill()
            box(l)
            end_fill()
        if self.ty == '+':
            fillcolor(255,153,0)
            pd()
            begin_fill()
            box(l)
            end_fill()
        if self.ty == '$':
            fillcolor(155,103,60)
            pd()
            begin_fill()
            crate(l)
            end_fill()
        if self.ty == '*':
            fillcolor(155,30,60)
            pd()
            begin_fill()
            crate(l)
            end_fill()        
        if self.ty == '@':
            fillcolor(255,100,255)
            pd()
            begin_fill()
            box(l)
            end_fill()
            
def main(n):
    pu()
    goto(-300,300)
    pd()
    color(255,255,255)
    begin_fill()
    box(1000)
    end_fill()
    pencolor(0,0,0)
    Lvlsplit = LevelList01[n].split('\n')
    NajduziString = len(Lvlsplit[0])
    for i in Lvlsplit:
        if len(i) > NajduziString:
            NajduziString = len(i)
        r = len(Lvlsplit)
        s = NajduziString
         
    #Making an empty matrix
    M0=[[0 for j in range(NajduziString)]for i in range(len(Lvlsplit))]
                
    #Playercoords
    #xcord = 0 L[0]
    #ycord = 0 L[1]
    L = [0,0]

    #Number of empty win cells
    global Winnum
    Winnum = [0]
                
    #Filling matrix with cell objects of correct type
    for i in range(r):
        for j in range(s):
            if j < len(Lvlsplit[i]):
                if Lvlsplit[i][j] == '@' or Lvlsplit[i][j] == '+':
                    L[1] = j
                    L[0] = i
                M0[i][j] = Cell(Lvlsplit[i][j])
                if Lvlsplit[i][j] == '.':
                    Winnum[0] += 1
            else:
                M0[i][j] = Cell(' ')

    #drawing the field
    for i in range(1):
        pu()
        goto(-300,ycor())
        pd()
        for j in range(s):
            M0[i][j].draw()
            fd(l)
    for i in range(1,r):
        pu()
        goto(-300,ycor() - l)
        pd()        
        for j in range(s):
            M0[i][j].draw()
            fd(l)

    #Win Condition
    def Wincheck():
        if Winnum[0] == 0:
            print('Press n')

    #Move turtle
    def upone(x,y):
        pu()
        goto(xcor() + l*y,ycor() - l*x)
        pd()
    def playercords():
        pu() 
        goto(-300 + (l*L[1]),300 - (l*L[0]))
        pd()    

    #player movement
    #movement functions
    def MoveUp():
        Move(0 , -1)
    def MoveDown():
        Move(0 , + 1)
    def MoveRight():
        Move(-1 , 0)
    def MoveLeft():
        Move(1 , 0)
        
    def Move(x,y):
        CellUp = M0[L[0] + y][L[1] + x]
        Cell2Up = M0[L[0] + 2*y][L[1] + 2*x]
        MyCell = M0[L[0]][L[1]]
        playercords()

        if MyCell.ty == '@':
            if CellUp.ty == ' ':
                MyCell.ty = ' '
                MyCell.draw()
                upone(y,x)
                CellUp.ty = '@'
                CellUp.draw()
                L[0] += y
                L[1] += x
                    
            elif CellUp.ty == '.':
                MyCell.ty = ' '
                MyCell.draw()
                upone(y,x)
                CellUp.ty = '+'
                CellUp.draw()
                L[0] += y
                L[1] += x
                    
            elif CellUp.ty == '$' and (Cell2Up.ty == ' ' or Cell2Up.ty == '.'):
                MyCell.ty = ' '
                MyCell.draw()
                upone(y,x)
                CellUp.ty = '@'
                CellUp.draw()
                upone(y,x)
                if Cell2Up.ty == ' ':
                    Cell2Up.ty = '$'
                    Cell2Up.draw()              
                elif Cell2Up.ty == '.':
                    Cell2Up.ty = '*'
                    Cell2Up.draw()
                    Winnum[0] -= 1
                L[0] += y
                L[1] += x

            elif CellUp.ty == '*' and (Cell2Up.ty == ' ' or Cell2Up.ty == '.'):
                MyCell.ty = ' '
                MyCell.draw()
                upone(y,x)
                CellUp.ty = '+'
                CellUp.draw()
                upone(y,x)
                if Cell2Up.ty == ' ':
                    Cell2Up.ty = '$'
                    Cell2Up.draw()
                    Winnum[0] += 1
                elif Cell2Up.ty == '.':
                    Cell2Up.ty = '*'
                    Cell2Up.draw()    
                L[0] += y
                L[1] += x
                
        elif MyCell.ty == '+':
            if CellUp.ty == ' ':
                MyCell.ty = '.'
                MyCell.draw()
                upone(y,x)
                CellUp.ty = '@'
                CellUp.draw()
                L[0] += y
                L[1] += x
                    
            elif CellUp.ty == '.':
                MyCell.ty = '.'
                MyCell.draw()
                upone(y,x)
                CellUp.ty = '+'
                CellUp.draw()
                L[0] += y
                L[1] += x
                    
            elif CellUp.ty == '$' and (Cell2Up.ty == ' ' or Cell2Up.ty == '.'):
                MyCell.ty = '.'
                MyCell.draw()
                upone(y,x)
                CellUp.ty = '@'
                CellUp.draw()
                upone(y,x)
                if Cell2Up.ty == ' ':
                    Cell2Up.ty = '$'
                    Cell2Up.draw()              
                elif Cell2Up.ty == '.':
                    Cell2Up.ty = '*'
                    Cell2Up.draw()
                    Winnum[0] -= 1
                L[0] += y
                L[1] += x

            elif CellUp.ty == '*' and (Cell2Up.ty == ' ' or Cell2Up.ty == '.'):
                MyCell.ty = '.'
                MyCell.draw()
                upone(y,x)
                CellUp.ty = '+'
                CellUp.draw()
                upone(y,x)
                if Cell2Up.ty == ' ':
                    Cell2Up.ty = '$'
                    Cell2Up.draw()
                    Winnum[0] += 1
                elif Cell2Up.ty == '.':
                    Cell2Up.ty = '*'
                    Cell2Up.draw()    
                L[0] += y
                L[1] += x
                
        Wincheck()

    listen(0,0)
    #Pressed buttons
    onkey(MoveUp,key="w")
    onkey(MoveDown,key="s")
    onkey(MoveRight,key="a")
    onkey(MoveLeft,key="d")
            


def Nextlvl():
    if Winnum[0] == 0:
        global Lvlnum
        Lvlnum += 1
        main(Lvlnum)

def Restart():
    global Lvlnum
    main(Lvlnum)
        
onkey(Nextlvl,key="n")
onkey(Restart,key="r")

main(0)
