def start():
    board = [{'a1':"a1","a2":"a2","a3":"a3"},{'b1':"b1","b2":"b2","b3":"b3"},{'c1':"c1","c2":"c2","c3":"c3"}]
    import random 
    letter= ["x","y"]
    p1=random.choice(letter)
    letter.remove(p1)
    p2=letter[0]
    print("player 1 is {} and player 2 is {} ".format(p1,p2))
    print(game_board(board))
#      player 1 date is processed when i is 1 and when i = 0 player 2 data is processed 
#      var z to calculate the number of successful data entry and filled fields
    i=1
    z =1
    while True : 
        if i == 1:
            player_1 = input("player 1 place  {}".format(p1))
            k1 = [*board[0].keys()]
            k2 = [*board[1].keys()]
            k3 = [*board[2].keys()]
            if player_1 in k1 and board[0][player_1]!="x" and board[0][player_1]!="y"  :
                board[0][player_1]=p1
            elif player_1 in k2 and board[1][player_1]!="x" and board[1][player_1]!="y" :
                 board[1][player_1]=p1
            elif player_1 in k3 and board[2][player_1]!="x" and board[2][player_1]!="y" :
                 board[2][player_1]=p1
            else :
                print("invalid input")
                continue
            print(game_board(board))

            end = checkwin(board)
            if end ==1 :
                print('congrats player 1 you are the winner')
                break 
            elif z==9:
                print("tied")
                break
            z=z+1
            i=0
        
        if i == 0:
            player_2 = input("player 2 place  {}".format(p2))
            k1 = [*board[0].keys()]
            k2 = [*board[1].keys()]
            k3 = [*board[2].keys()]
            if player_2 in k1 and board[0][player_2]!="x" and board[0][player_2]!="y"  :
                 board[0][player_2]=p2
            elif player_2 in k2 and board[1][player_2]!="x" and board[1][player_2]!="y" :
                 board[1][player_2]=p2
            elif player_2 in k3 and board[2][player_2]!="x" and board[2][player_2]!="y" :
                 board[2][player_2]=p2
            else :
                print("invalid input")
                continue
            print(game_board(board))
            end = checkwin(board)
            if end ==1 :
                print('congrats player 2 you are the winner')
                break  
            elif z ==9:
                print("tied")
                break
            z=z+1
            i=1

def game_board(board):
      
    gm_board= ""
    for i in board:
        k=i.keys()
        
        for ele in k :
            gm_board+= i[ele]+'   '
        gm_board+="\n"
    return gm_board


def checkwin(board):
      
    for ele in board :
        keys =[*ele.keys()]
        val = [*ele.values()]
        if ele[keys[0]] == ele[keys[1]] == ele[keys[2]] :
            return 1
                     
    if board[0]["a1"]==board[1]["b1"]==board[2]["c1"] or board[0]["a2"]==board[1]["b2"]==board[2]["c2"] or board[0]["a3"]==board[1]["b3"]==board[2]["c3"] or board[0]["a1"]==board[1]["b2"]==board[2]["c3"] or board[0]["a3"]==board[1]["b2"]==board[2]["c1"] :
        return 1 
start()     
