from tkinter import *
import random
from tkinter import ttk
import math

#newwindow
Gamewindow=Tk()

Gamewindow.title('Games')

tabs = ttk.Notebook(Gamewindow)

Gamewindow.config(bg ='turquoise')

#----------------------------------------------------------Memory Puzzle-------------------------------------------------------------

Memorypuzzle= ttk.Frame(tabs)


#shapes
def draw(a,l,m):
    global base
    if a=='A':
        d=base.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20, fill='red')
    elif a=='B':
        d=base.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20, fill='yellow')
    elif a=='C':
        d=base.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20, fill='blue')
    elif a=='D':
        d=base.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20, fill='red')
    elif a=='E':
        d=base.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20, fill='yellow')
    elif a=='F':
        d=base.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20, fill='blue')
    elif a=='G':
        d=base.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20, fill='red')
    elif a=='H':
        d=base.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20, fill='green')

#to play   
def quizboard():
    global base,ans,board,moves
    count=0
    for i in range(4):
        for j in range(4):
            rec=base.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="white")
            if(board[i][j]!='.'):
                draw(board[i][j],i,j)
                count+=1
    if count==16:
        base.create_text(200,450,text="Number of moves: "+str(moves), font=('arial',20))
            

def call(event):
    global base,ans,board,moves,prev
    i=event.x//100
    j=event.y//100
    if board[i][j]!='.':
        return
    moves+=1

    #print(moves)
    if(prev[0]>4):
        prev[0]=i
        prev[1]=j
        board[i][j]=ans[i][j]
        quizboard()
    else:
        board[i][j]=ans[i][j]
        quizboard()
        if(ans[i][j]==board[prev[0]][prev[1]]):
            print("matched")
            prev=[100,100]
            quizboard()
            return
        else:
            board[prev[0]][prev[1]]='.'
            quizboard()
            prev=[i,j]
            return

base=Canvas(Memorypuzzle,width=500,height=500)
base.pack()

ans = list('AABBCCDDEEFFGGHH')
random.shuffle(ans)
ans = [ans[:4],
       ans[4:8],
       ans[8:12],
       ans[12:]]

base.bind("<Button-1>", call)

moves=IntVar()
moves=0

prev=[100,100]

board=[list('.'*4) for count in range(4)]

#exit
def Exit():
    Gamewindow.destroy()


Button(Memorypuzzle, font = 'times 15 bold', text = 'EXIT' , padx =5, bg ='light grey' , command = Exit).place(x=400,y=450)

quizboard()

#-----------------------------------------------------------Rock Paper Scissors----------------------------------------------------

Rockpaper= ttk.Frame(tabs)
 
tabs.add(Memorypuzzle, text ='Memory Puzzle Game') 
tabs.add(Rockpaper, text ='Rock Paper Scissors')  
tabs.pack(expand = 1, fill ="both") 


Label(Rockpaper, text = 'Rock, Paper, Scissors' , font='tinmes 20 bold', bg = 'light grey').place(x = 90,y=10)

#user
user_take = StringVar()
Label(Rockpaper, text = 'Choose any one: Rock, Paper, Scissors' , font='times 15 bold', bg = 'light grey').place(x = 60,y=70)
Entry(Rockpaper, font = 'arial 15', textvariable = user_take , bg = 'white').place(x=130 , y = 130)


#computer
comp = random.randint(1,3)
if comp == 1:
    comp = 'rock'
elif comp ==2:
    comp = 'paper'
else:
    comp = 'scissors'
    
#to play
Result = StringVar()

def quizboard2():
    user = user_take.get()
    if user == comp:
        Result.set('tie, you both selected the same')
    elif user == 'rock' and comp == 'paper':
        Result.set('you loose, the computer selected paper')
    elif user == 'rock' and comp == 'scissors':
        Result.set('you win, the computer selected scissors')
    elif user == 'paper' and comp == 'scissors':
        Result.set('you loose, the computer selected scissors')
    elif user == 'paper' and comp == 'rock':
        Result.set('you win, the computer selected rock')
    elif user == 'scissors' and comp == 'rock':
        Result.set('you loose, the computer selected rock')
    elif user == 'scissors' and comp == 'paper':
        Result.set('you win, the computer selected paper')
    else:
        Result.set('invalid: choose any one - rock, paper, scissors')
    
#reset
def Reset():
    Result.set("") 
    user_take.set("")

#exit
def Exit():
    Gamewindow.destroy()

#buttons
Entry(Rockpaper, font = 'arial 12 bold', textvariable = Result, bg ='white',width = 45,).place(x=45, y = 290)

Button(Rockpaper, font = 'times 15 bold', text = 'PLAY' , padx =5, bg ='light grey' , command = quizboard2).place(x=200,y=210)

Button(Rockpaper, font = 'times 15 bold', text = 'RESET' , padx =5, bg ='light grey' , command = Reset).place(x=90,y=350)

Button(Rockpaper, font = 'times 15 bold', text = 'EXIT' , padx =5, bg ='light grey' , command = Exit).place(x=350,y=350)

#-----------------------------------------------------Guess number game-----------------------------------------------------------

Guessnumber= ttk.Frame(tabs)
 
tabs.add(Memorypuzzle, text ='Memory Puzzle Game') 
tabs.add(Rockpaper, text ='Rock Paper Scissors')
tabs.add(Guessnumber, text ='Guess the Number')
tabs.pack(expand = 1, fill ="both") 


Label(Guessnumber, text = 'Guessing the Number Game' , font='tinmes 20 bold', bg = 'light grey').place(x = 70,y=10)

#user
guess = IntVar()
Label(Guessnumber, text = 'Guess a number:' , font='times 15 bold', bg = 'light grey').place(x = 170,y=70)
Entry(Guessnumber, font = 'arial 15', textvariable = guess , bg = 'white').place(x=130 , y = 130)

#computer
x = random.randint(1, 100)
    
#to play
Value = StringVar()

def quizboard3():
    usernum = guess.get()
    
    if x == usernum:
        Value.set('Congratulations you did it!')
    elif x > usernum:
        Value.set('You guessed too low!')
    elif x < usernum:
        Value.set('You guessed too high!')
 

#reset
def Reset():
    Value.set("") 
    guess.set()

#exit
def Exit():
    Gamewindow.destroy()

#buttons
Entry(Guessnumber, font = 'arial 12 bold', textvariable = Value, bg ='white',width = 45,).place(x=45, y = 290)

Button(Guessnumber, font = 'times 15 bold', text = 'PLAY', padx =5, bg ='light grey', command = quizboard3).place(x=200,y=210)

Button(Guessnumber, font = 'times 15 bold', text = 'RESET', padx =5, bg ='light grey', command = Reset).place(x=90,y=350)

Button(Guessnumber, font = 'times 15 bold', text = 'EXIT', padx =5, bg ='light grey', command = Exit).place(x=350,y=350)


mainloop()