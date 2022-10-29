import random
def drawboard(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])
def inputletter():
    print('do you want x or o?')
    letter=input().upper()
    if(letter=='X'):
        return ['X','O']
    else:
        return ['O','X']
def whogoesfirst():
    if(random.randint(0,1)==0):
        return 'computer'
    else:
        return 'player'
def getplayermove(board):
    move=''
    while((move not in '1 2 3 4 5 6 7 8 9'.split()) or (not isspacefree(board,int(move)))):
        print('what is next move')
        move=input()
    return int(move)
def isspacefree(board,move):
    return board[move]==''
def makemove(board,s,move):
    board[move]=s
def iswinner(b,p):
    return ((b[1]==p and b[2]==p and b[3]==p) or
            (b[4]==p and b[5]==p and b[6]==p) or
            (b[7]==p and b[8]==p and b[9]==p) or
            (b[1]==p and b[4]==p and b[7]==p) or
            (b[2]==p and b[5]==p and b[8]==p) or
            (b[3]==p and b[6]==p and b[9]==p) or
            (b[1]==p and b[5]==p and b[9]==p) or
            (b[7]==p and b[5]==p and b[3]==p)
            )
def playagain():
    print('do you want to play again?')
    a=input().lower()
    if(a.startswith('y')):
        return True
    return False
def getBoardcopy(board):
    db=[]
    for i in board:
        db.append(i)
    return db
def getcomputermove(board,c,p):
    for i in range(1,10):
        copy=getBoardcopy(board)
        if(isspacefree(copy,i)):
            makemove(copy,c,i)
            if(iswinner(copy,c)):
                return i
    for i in range(1,10):
        copy=getBoardcopy(board)
        if(isspacefree(copy,i)):
            makemove(copy,p,i)
            if(iswinner(copy,p)):
                return i
    move=chooserandommoves(board,[1,3,7,9])
    if(move!=None):
        return move
    if(isspacefree(board,5)):
        return 5
    return chooserandommoves(board,[2,4,6,8])
def chooserandommoves(board,movelist):
    pm=[]
    for i in movelist:
        if(isspacefree(board,i)):
            pm.append(i)
    if(len(pm)!=0):
        return random.choice(pm)
    else:
        return None
def boardfull(board):
    for i in range(1,10):
        if(isspacefree(board,i)):
            return False
    return True
print('welcome to tic tac toe game')
while(True):
    board=['']*10
    p,c=inputletter()
    turn=whogoesfirst()
    print(turn+" goes first")
    gameisplaying=True
    while(gameisplaying):
        if(turn=='player'):
            move=getplayermove(board)
            makemove(board,p,move)
            drawboard(board)
            if(iswinner(board,p)):
                drawboard(board)
                print('-------------')
                print('player won')
                gameisplaying=False
            else:
                if(boardfull(board)):
                    drawboard(board)
                    print('its a tie')
                    print('-------------')
                    gameisplaying=False
                else:
                    turn='computer'
        else:
            move=getcomputermove(board,c,p)
            makemove(board,c,move)
            print('after move')
            drawboard(board)
            print('-------------')
            if(iswinner(board,c)):
                drawboard(board)
                print('computer won')
                print('-------------')
                gameisplaying=False
            else:
                if(boardfull(board)):
                    print('its a tie')
                    drawboard(board)
                    print('-------------')
                    gameisplaying=False
                else:
                    turn='player'
    
    if not playagain():
        break
            
                
            
            
    
    
            
    