player1 = input("Player 1 :  " )
player2 = input("Player 2 : " )

if (player1 == "Rock" and player2 == "Scissors"):
    print ("Player 1 Wins")
elif (player1 == "Scissors" and player2 == "Paper"):
    print ("Player 1 Wins")
elif (player1 == "Paper" and player2 == "Rock"):
    print ("player 1 Wins")
else:
    print ("Player 2 wins")

Newgame = input("Do you want to start a new game :" )