

li=[1,2,3,4,5,6,7,8,9]
wins =[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
player ='X'
flag = 0
count = 0
while True:
    print("\n\tTIC-TAC-TOE")
    print(f"\n\t {li[0]} | {li[1]} | {li[2]} ")
    print("\t------------")
    print(f"\t {li[3]} | {li[4]} | {li[5]} ")
    print("\t------------")
    print(f"\t {li[6]} | {li[7]} | {li[8]} ")
    if flag==1:
        break
    if count==9:
        print("\n\tMATCH TIE")
        break      
    ch=int(input(f"\n     Player {player} Turns : "))
    if ch in li:
        li[ch-1] = player
        count=count+1
        for a,b,c in wins:
            if li[a]==li[b]==li[c]:
                print(f"\t\n\tplayer {player} WINS")
                flag = 1
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    else:
        print("\n\tNo Cheating..")
        
     
