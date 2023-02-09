print("Exam Grade Calculator")
exam = input("Name of exam:")
MaxScore = int(input("What is the Possible Score:"))
YourScore = int(input("What is your score:"))
Percentage = YourScore/MaxScore * 100
if Percentage >= 90:
  print("You got {:.2f}% which is a A+".format(Percentage))
elif 80<= Percentage <90:
  print("You got {:.2f}% which is a A".format(Percentage))
elif 70<= Percentage <80:
  print("You got {:.2f}% which is a B".format(Percentage))
elif 60<= Percentage <70:
  print("You got {:.2f}% which is a C".format(Percentage))
elif 50<= Percentage <60:
  print("You got {:.2f}% which is a D".format(Percentage))
elif 40<= Percentage <50:
  print("You got {:.2f}% which is a U".format(Percentage))
else:
  print("You're failed")
