#Mine sweeper
#Mine sweeper
from turtle import*
from random import*

#Crtanje sahovnice
title('Mine Sweeper')
duljina=20 #duljina polja
x0=-200 #gornja lijeva tocka
y0=200 #gornja lijeva tocka
x=x0
y=y0
colormode(255)
uvjet_pobjede=324
tracer(False)
fillcolor('grey')
begin_fill()
pu()
goto(x0,y0)
pd()
for i in range(4):
    fd(400)
    rt(90)
end_fill()

seth(0)
for i in range(21):
    pu()
    goto(x,y)
    pd()
    fd(20*duljina)
    y-=20
x=x0
y=y0  
for i in range(21):
    seth(270)
    pu()
    goto(x,y)
    pd()
    fd(20*duljina)
    x+=20

#Matrica
r=18
s=18
def ispis_mat(r,s,M):
    for i in range(r):
        for j in range(s):
            print(M[i][j],end=' ')
        print()
    print(sep=' ')
M=[[0 for j in range(s)]for i in range(r)]

def polje(duljina):
    for i in range(4):
        fd(duljina)
        rt(90)


#Crtanje zidova
fillcolor(randint(180,255),randint(180,255),randint(180,255))
seth(0)
x=x0
y=y0
for i in range(2):
    for j in range(20):
        pu()
        goto(x+(j*duljina),y)
        pd()
        begin_fill()
        polje(duljina)
        end_fill()
    y=-y+20
for i in range(2):
    for j in range(20):
        pu()
        goto(x,y-(j*duljina))
        pd()
        begin_fill()
        polje(duljina)
        end_fill()
    x=-x-20
    
#Crtanje bombi
def bomba(r,y):
    tracer(False)
    pu()
    sety(y-r)
    pd()
    color('black')
    begin_fill()
    for i in range(4):
        circle(r,90)
        rt(90)
        fd(r//2)
        rt(180)
        fd(r//2)
        rt(90)
    end_fill()
    tracer(True)

#Tablica zastavica
ZM=[[0 for j in range(18)]for i in range(18)]

#Bombe i okolo njih
max_br_bombi=int(input('Upisi tezinu igre: Normal - 50, Hard - 65, Expert - 80'))
br_bombi=max_br_bombi
while br_bombi>0:
    rand_redak=randint(0,17)
    rand_stupac=randint(0,17)
    if M[rand_redak][rand_stupac]!='.':
        M[rand_redak][rand_stupac]='.'
        for i in range(rand_redak-1,rand_redak+2):
            for j in range(rand_stupac-1,rand_stupac+2):
                if i<18 and i>=0 and j<18 and j>=0:
                    if M[i][j]!='.':
                        M[i][j]+=1
                
        br_bombi-=1

#Postavljanje zastavica
def zastavica(x,y):
    tracer(False)
    pu()
    goto(x-8,y-6)
    pd()
    fd(16)
    lt(180)
    fd(8)
    rt(90)
    fd(6)
    kut=110
    fillcolor('red')
    begin_fill()
    for i in range(3):
        fd(8)
        lt(kut)
        kut+=30
    end_fill()
    tracer(True)
    
def koordinate_u_matrici(x_klik,y_klik): #Uzima koordinate klika i vraca koordinate iscrtavanja
    lijeviX=-180
    desniX=-160
    gornjiY=180
    donjiY=160
    x_koordinata_polja=-1
    y_koordinata_polja=-1
    imamo_koord=False
    for i in range(18):
        if imamo_koord==True:
            break
        for j in range(18):
            if lijeviX<=x_klik and x_klik<=desniX and gornjiY>=y_klik and y_klik>=donjiY:
                x_koordinata_polja,y_koordinata_polja=i,j
                imamo_koord=True
                break
            lijeviX+=duljina
            desniX+=duljina
        lijeviX=-180
        desniX=-160
        gornjiY-=duljina
        donjiY-=duljina
        
    sredX=-170
    sredY=170
    imamo_koord=False
    for i in range(18):
        if imamo_koord==True:
            break
        for j in range(18):
            if x_koordinata_polja==i and y_koordinata_polja==j:
                Zeljena_x_pozicija=sredX
                Zeljena_y_pozicija=sredY
                imamo_koord=True
                break
            sredX+=duljina
        sredX=-170
        sredY-=duljina
    return x_koordinata_polja,y_koordinata_polja,Zeljena_x_pozicija,Zeljena_y_pozicija
    
def postavi_zastavicu(x_klik,y_klik):
    x_kordinata_matrice,y_kordinata_matrice,Zeljena_x_pozicija,Zeljena_y_pozicija=koordinate_u_matrici(x_klik,y_klik)
    crtanje_zastavice(x_kordinata_matrice,y_kordinata_matrice,Zeljena_x_pozicija,Zeljena_y_pozicija)
    
onscreenclick(postavi_zastavicu,btn=3)

def crtanje_zastavice(x_koordinata_polja,y_koordinata_polja,Zeljena_x_pozicija,Zeljena_y_pozicija):
    if ZM[x_koordinata_polja][y_koordinata_polja]==0:
        pu()
        goto(Zeljena_x_pozicija,Zeljena_y_pozicija-duljina)
        pd()
        seth(0)
        zastavica(Zeljena_x_pozicija,Zeljena_y_pozicija)
        ZM[x_koordinata_polja][y_koordinata_polja]=1
        win_condition()
    elif ZM[x_koordinata_polja][y_koordinata_polja]==1:
        seth(0)
        tracer(False)
        pu()
        goto(Zeljena_x_pozicija-10,Zeljena_y_pozicija-10)
        pd()
        fillcolor('grey')
        begin_fill()
        for i in range(4):
            fd(20)
            lt(90)
        end_fill()
        tracer(True)
        ZM[x_koordinata_polja][y_koordinata_polja]=0
        
#LMB klik(otvaranje polja)
def klik(x_klik,y_klik):
    x_kordinata_matrice,y_kordinata_matrice,Zeljena_x_pozicija,Zeljena_y_pozicija=koordinate_u_matrici(x_klik,y_klik)
    print(x_kordinata_matrice,y_kordinata_matrice,Zeljena_x_pozicija,Zeljena_y_pozicija)
    otvaranje_polja(x_kordinata_matrice,y_kordinata_matrice,Zeljena_x_pozicija,Zeljena_y_pozicija)
    
onscreenclick(klik)

#Crtanje otvorenog polja
def otvaranje_polja(x_koordinata_polja,y_koordinata_polja,Zeljena_x_pozicija,Zeljena_y_pozicija):
    if M[x_koordinata_polja][y_koordinata_polja]=='.' and ZM[x_koordinata_polja][y_koordinata_polja]==0:
        game_over()
    elif M[x_koordinata_polja][y_koordinata_polja]==0 and ZM[x_koordinata_polja][y_koordinata_polja]==0:
        nularek(x_koordinata_polja,y_koordinata_polja,Zeljena_x_pozicija,Zeljena_y_pozicija)
    elif M[x_koordinata_polja][y_koordinata_polja]!=0 and ZM[x_koordinata_polja][y_koordinata_polja]==0:
        tracer(False)
        pu()
        goto(Zeljena_x_pozicija-10,Zeljena_y_pozicija+10)
        pd()
        seth(0)
        fillcolor('white')
        begin_fill()
        polje(duljina)
        end_fill()
        pu()
        goto(Zeljena_x_pozicija,Zeljena_y_pozicija-duljina/2)
        seth(0)
        write(M[x_koordinata_polja][y_koordinata_polja],move=True,align='center')
        pd()
        tracer(True)
        ZM[x_koordinata_polja][y_koordinata_polja]=2
        win_condition()


        
        
#Otvaranje '0'
def nularek(x,y,Zeljena_x_pozicija,Zeljena_y_pozicija):
    if x<18 and x>=0 and y<18 and y>=0:
        if M[x][y]!=0:
            otvaranje_polja(x,y,Zeljena_x_pozicija,Zeljena_y_pozicija)
            return
        elif M[x][y]==0 and ZM[x][y]!='n' and x<=18 and x>=0 and y<=18 and y>=0:
            tracer(False)
            pu()
            goto(Zeljena_x_pozicija-10,Zeljena_y_pozicija+10)
            pd()
            seth(0)
            fillcolor('white')
            begin_fill()
            polje(duljina)
            end_fill()
            tracer(True)
            ZM[x][y]='n'
            win_condition()
            nularek(x+1,y,Zeljena_x_pozicija,Zeljena_y_pozicija-20)
            nularek(x,y-1,Zeljena_x_pozicija-20,Zeljena_y_pozicija)
            nularek(x,y+1,Zeljena_x_pozicija+20,Zeljena_y_pozicija)
            nularek(x-1,y,Zeljena_x_pozicija,Zeljena_y_pozicija+20)
            nularek(x+1,y+1,Zeljena_x_pozicija+20,Zeljena_y_pozicija-20)
            nularek(x+1,y-1,Zeljena_x_pozicija-20,Zeljena_y_pozicija-20)
            nularek(x-1,y+1,Zeljena_x_pozicija+20,Zeljena_y_pozicija+20) 
            nularek(x-1,y-1,Zeljena_x_pozicija-20,Zeljena_y_pozicija+20)
            return
        
#Kraj
def game_over():
    x_180=-180
    y_180=180
    pu()
    goto(x_180,y_180)
    pd()
    seth(0)
    for i in range(r):
        for j in range(s):
            if M[i][j]!=0 and M[i][j]!='.' and ZM[i][j]==0:
                tracer(False)
                pu()
                goto(x_180+j*20,y_180-i*20)
                pd()
                fillcolor('white')
                begin_fill()
                polje(duljina)
                end_fill()
                pu()
                goto(x_180+10+j*20,y_180-20-i*20)             
                write(M[i][j],move=True,align='center')
                pd()   
                tracer(True)
            elif M[i][j]=='.':
                tracer(False)
                pu()
                goto(x_180+10+j*20,y_180-i*20)
                pd()
                seth(0)
                bomba(duljina/4,y_180-10-i*20)
                tracer(True)
            elif M[i][j]==0:
                tracer(False)
                pu()
                goto(x_180+j*20,y_180-i*20)
                pd()
                fillcolor('white')
                begin_fill()
                polje(duljina)
                end_fill()                
                tracer(True)
    pu()
    goto(0,-280)
    write('GAME OVER',move=True,align='center',font=('Arial',30,'normal'))
    pd()
    
def win_condition():
    win=True
    br_zastavica=0 
    for i in range(18):
        for j in range(18):
            if ZM[i][j]==1:
                br_zastavica+=1     
            if ZM[i][j]==0:
                win=False

    if win==True and br_zastavica==max_br_bombi:
        pu()
        goto(0,-280)
        write('WIN',move=True,align='center',font=('Arial',30,'normal'))
        pd()
                
speed(10)
ht()
tracer(True)
