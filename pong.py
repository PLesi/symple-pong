from tkinter import *
from random import *


c = Canvas(width=600,height=400,bg = '#515252')
c.pack()



title = True

ballSpeed = 6
Xmove = -ballSpeed
Ymove = -ballSpeed

playerSpeed = 15

Game = True
gameOver = False

GoodEnd = 0
waitForAnsw = False

p1ScoreInt = 0
p2ScoreInt = 0

i = 0

p1Color = ['red','green','blue']
p1BaseColor = 'white'
p2BaseColor = 'white'

Font_tuple = ("Comic Sans MS", 15, "bold")

titleBg = c.create_rectangle(-10,-10,610,410,fill='black',tags='uwu')

titleTxt = c.create_text(300,160,font='Impact 50 bold',fill='white',text='PONG')
titleCred = c.create_text(300,360,font=Font_tuple,fill='white',text='by Michal Pleško')

titleBtn = c.create_rectangle(200,230,295,270,fill='grey',outline='white',width=5)
titleBtnEx = c.create_rectangle(305,230,400,270,fill='grey',outline='white',width=5)

titleBtnTxt = c.create_text(295-47.5,250,text='START',font='Arial 20 bold',fill='white')
titleBtnExtTxt = c.create_text(305+47.5,250,text='EXIT',font='Arial 20 bold',fill='white')


if title:
    Btn1Loc = c.coords(titleBtn)
    Btn2Loc = c.coords(titleBtnEx)
    def click(event):
        global title,Font_tuple
        if event.x > Btn1Loc[0] and event.x < Btn1Loc[2] and event.y > Btn1Loc[1] and event.y < Btn1Loc[3]:
            c.delete('all')
            title = False
            game()
        elif event.x > Btn2Loc[0] and event.x < Btn2Loc[2] and event.y > Btn2Loc[1] and event.y < Btn2Loc[3]: 
            def again(event):
                Btn.place(x=randint(20,380),y=randint(20,380))
            def nwm():
                Exit.destroy()

            Exit = Toplevel()
            Exit.geometry('400x400')
            Txt = Label(Exit,text = 'do you realy want exit?',font=Font_tuple)
            Txt.place(x=100,y=50)
            Btn = Button(Exit,text='YES',font=Font_tuple,foreground='#E13317')
            Btn.bind('<Enter>',again)
            Btn.place(x=100,y=100)
            BtnExit = Button(Exit,text='NO',font='Arial 20 bold',foreground='#46E117',command=nwm)
            BtnExit.place(x=200,y=100)
            
            

    print(Btn1Loc,Btn2Loc)
    c.bind('<Button-1>',click)
def game():
    global ballSpeed,Xmove,Ymove,playerSpeed,Game,gameOver,p1ScoreInt,p2ScoreInt,p1BaseColor,p2BaseColor,p2Score,ball,player,enemy
    c.create_line(300,0,300,400,width=5,fill='white')

    TopWall = c.create_rectangle(0,0,600,5,fill='white',tags='Twall')
    BottomWall = c.create_rectangle(0,395,600,400,fill='white',tags='Bwall')

    player = c.create_rectangle(16,165,22,235,fill=p1BaseColor,tags='p1')
    enemy = c.create_rectangle(584,165,578,235,fill=p2BaseColor, tags='p2')

    p1Score = c.create_text(150,25,text=p1ScoreInt,font='Arial 30 bold',fill='#00EEFF')
    p2Score = c.create_text(450,25,text=p2ScoreInt,font='Arial 30 bold',fill='#FF4500')

    ball = c.create_oval(290,190,310,210,fill='#15FF00',outline='black',width=2,tags='ballTag')

    def win():
        global p1ScoreInt,Ymove,Xmove,gameOver
        p1ScoreInt += 1
        c.itemconfig(p1Score,text=p1ScoreInt)

        c.coords(ball,290,190,310,210)
        c.coords(player,16,165,22,235)
        c.coords(enemy,584,165,578,235)

        ballSpeed = 5
        Xmove = +ballSpeed
        Ymove = -ballSpeed

        if p1ScoreInt == 3:
            c.create_text(300,200,font='Phosphate 50',text='GAME OVER',fill='#19FFF6')
            c.create_text(300,250,font='Phosphate 25',text='WINNER',fill='#19FFF6')
            gameOver = True

    def lose():
        global p2ScoreInt,Xmove,Ymove,player,enemy,ball,p2Score,ballSpeed,gameOver
        
        p2ScoreInt +=1
        c.itemconfig(p2Score,text=p2ScoreInt)
        
        c.coords(ball,290,190,310,210)
        c.coords(player,16,165,22,235)
        c.coords(enemy,584,165,578,235)

        ballSpeed = 5
        Xmove = -ballSpeed
        Ymove = -ballSpeed

        if p2ScoreInt == 3:
            c.create_text(300,200,font='Phosphate 50',text='GAME OVER',fill='#FF6817')
            c.create_text(300,250,font='Phosphate 25',text='LOSER',fill='#FF6817')
            gameOver = True

    def moveUp(event):
        globals()
        c.move(player,0,-playerSpeed)


    def moveDown(event):
        globals()
        c.move(player,0,playerSpeed)


    c.bind_all('<Up>',moveUp)
    c.bind_all('<Down>',moveDown)


    while Game == True:

        c.move(ball,Xmove,Ymove)

        if Ymove > 0:
            a = random()
            if a > 0.70:
                enemySpeed = Ymove - 3.5
            else:
                enemySpeed = Ymove
        elif Ymove < 0:
            a = random()
            if a > 0.70:
                enemySpeed = Ymove + 3.5
            else:
                enemySpeed = Ymove
            
        c.move(enemy,0,enemySpeed)

        BallLoc = c.coords('ballTag')
        P1Loc = c.coords('p1')
        P2Loc = c.coords('p2')
        TWall = c.coords('Twall')
        BWall = c.coords('Bwall')

        print("player: ",P1Loc)
        print("Ball: ",BallLoc)


        if P1Loc[1] < 0:
            c.coords(player,16,0,22,70)
        elif P1Loc[3] > 400:
            c.coords(player,16,330,22,400)
        
        if P2Loc[1] < 0:
            c.coords(enemy,584,0,578,70)
        elif P2Loc[3] > 400:
            c.coords(enemy,584,330,578,400)


        if BallLoc[0] <= P1Loc[2] and BallLoc[3] >= P1Loc[1] and BallLoc[3] <= P1Loc[3] and BallLoc[2] > P1Loc[0]:    
            print('uwu')
            c.itemconfig(player,fill='#39FF14')
            Xmove *= -1
            Xmove += 1

        elif BallLoc[2] >= P2Loc[0] and P2Loc[1] <= BallLoc[1] and BallLoc[1] <= P2Loc[3] and BallLoc[0] < P2Loc[2]:
            print('owo')
            c.itemconfig(enemy,fill='#59f1ff')
            Xmove *= -1
            ballSpeed += 0.1
            
        elif BallLoc[1] <= TWall[3]:
            c.itemconfig(TopWall,fill='#FF5F1F')
            Ymove *= -1

        elif BallLoc[3] >= BWall[3]:
            c.itemconfig(BottomWall,fill='#FF5F1F')
            Ymove *= -1
        
        elif BallLoc[2] < P1Loc[0]:
            lose()
            

        elif BallLoc[0] > P2Loc[2]:
            win()

        else:
            c.itemconfig(player,fill='white')
            c.itemconfig(enemy,fill='white')
            c.itemconfig(TopWall,fill='white')
            c.itemconfig(BottomWall,fill='white')

        if gameOver == True:
            c.move(player,0,Ymove)



        c.after(50)
        c.update()



mainloop()
