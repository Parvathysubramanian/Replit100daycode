print("Fill-in the blank !")
print("(type in the blank. see if you're as cool s me)")

counter =0
while True: 
  first_question = input("The Capital of France is _______: ")
  counter +=1
  if first_question =="Paris":
    break
print("Great, you got the answer in",counter,"attempt")

#print should allign with the while statement or else it will even just read the wrong one as correct one 

counter =0
while True:   
  second_question = int(input("The number of planets in our solar system is _____."))
  counter +=1
  if second_question =="Eight" or second_question =="8":
    break
print("Great, you got the answer in",counter,"attempt")

counter =0
while True:
  third_question = input("The largest ocean on Earth is called the _____.")
  counter +=1
  if third_question =="Pacific ocean":
    break
print("Great, you got the answer in",counter,"attempt")
    
counter = 0
while True:
  fourth_question = input("The famous painting The Starry Night was created by _____.")
  counter +=1
  if fourth_question =="Vincent van Gogh":
    break
print("Great, you got the answer in",counter,"attempt")
    
counter = 0
while True:
  fifth_question = input("The currency used in Japan is called the _____.")
  counter += 1
  if fifth_question == "Yen":
    break
print("Great, you got the answer in",counter,"attempt")
