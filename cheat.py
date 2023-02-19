print("E P I C   🪨  🗞️  ✂️    B A T T L E")
print("Round 1")
print("Select your move (R, P or S)")

Player1 =0
Player2 =0

while True: 
  Player1_round = input("Player 1 >")
  Player2_round = input("Player 2 >")
  
  if Player1_round =="R" and Player2_round == "P":
    print("Player 1 won")
    Player1 +=1
  elif Player1_round =="R" and Player2_round =="S":
    print("Player 1 won")
    Player1 +=1
  elif Player1_round =="S" and Player2_round == "P":
    print("Player 1 won")
    Player1 +=1
  elif Player1_round =="R" and Player2_round =="R":
   print("It's a tie")
  elif Player1_round =="P" and Player2_round =="P":
    print("Its a Tie")
  if Player1_round =="P" and Player2_round =="S":
    print("Player 2 won")
    Player2 +=1
  elif Player1_round =="P" and Player2_round =="R":
    print("Player 2 won")
    Player2 +=1
  elif Player1_round == "S" and Player2_round =="R":
    print("Player 2 won")
    Player2 +=1

  if Player1 == 3 or Player2 == 3:
    print("Thanks for playing")
    exit()
    
  else:
    print("Player 1 has", Player1, "wins")
    print("Player 2 has", Player2, "wins")
    continue
