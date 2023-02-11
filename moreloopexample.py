#Write a program that continuously asks the user for a number and calculates the sum of all numbers entered until the user enters 'q' to quit

print("Addition")

exit ="q"
while exit == "q":
  number1 = int(input("What is the first digit you want to sum: "))
  number2 = int(input("What is the second digit you want to sum: "))
  sum = int(number1 + number2)
  print(sum)
  exit = input("If you want to quit, enter q :")
