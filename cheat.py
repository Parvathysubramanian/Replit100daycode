print("E P I C   🪨  🗞️  ✂️    B A T T L E")
print("Round 1")
print("Select your move (R, P or S)")
while True:
  counter = 0
  Player1 = input("Player 1 >")
  Player2 = input("Player 2 >")
  if Player1 =="R" and Player2 == "P":
    print("Player 1's Rock is smothered by Player 2's Paper")
  elif Player1 =="R" and Player2 =="S":
   print("Player 1's Rock is smothered by Player 2's Scissors")
  elif Player1 =="R" and Player2 =="R":
   print("It's a tie")
  elif Player1 =="P" and Player2 =="P":
    print("Its a Tie")
  elif Player1 =="P" and Player2 =="R":
    print("Player 2's Rock is smothered by Player 1's Paper")
  elif Player1 =="P" and Player2 =="S":
    print("Player 1's Paper is smothered by Player 2's Scissors")
  elif Player1 == "S" and Player2 =="R":
    print("Player 2's Rock is smothered by Player 1's Scissor")
  elif Player 1 =="S" and Player2 == "P":
  print("Player 1's Scissor is smothered by Player 2's Paper")
  break
print("Try again")
counter +=1
print(counter)
