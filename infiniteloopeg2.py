#Write a program that repeatedly asks the user for their favorite color until they type "exit".

exit ="no"
while exit =="no":
  
  fav_color = input("What is your favorite colour?")
  if fav_color == "Red":
    print("Red is a vibrant color that symbolizes passion and energy.")
  elif fav_color =="Blue":
   print("Blue is a serene color that represents trust, stability, and security.")
  
  elif fav_color =="Orange":
    print("Orange is a warm and cheerful color that brings positivity to your life.")

  elif fav_color =="Green":
    print("Green is a fresh and calming color that represents growth and renewal.")

  else:
    print("I am sorry, i dont know the definition of your favourite color")
    exit = input("Do you wnat to exit the game?: ")
        
