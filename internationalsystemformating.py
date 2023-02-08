year = int(input("Lets check the the total seconds in the year, What is the year?"))
if year % 4 == 0 and year % 100 and year % 400 ==0:
  totalLseconds = 366*24*60*60
  formatedLNumber ="{:,}".format(totalLseconds)
  print("The total seconds in a leap year is", formatedNLNumber)
      
else:
  totalNseconds = 365*24*60*60
  formatedNLNumber ="{:,}".format(totalNseconds)
  print("The total seconds in a non leap year is",formatedNLNumber)
