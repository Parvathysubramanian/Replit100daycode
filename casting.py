print("Generation Identifier")
birthyear = int(input("Which year were you born?"))
if birthyear in range(1883,1900):
  print("You're in Lost Generation")
elif birthyear in range(1901,1927):
  print("You're in a Greatest Generation")
elif birthyear in range(1928,1945):
  print("You're in a Silent Generation")
elif birthyear in range(1946,1964):
  print("You're in a Baby Boomers")
elif birthyear in range(1965,1980):
  print("You're in Generation X")
elif birthyear in range(1981,1996):
  print("You're in Millennials")
elif birthyear in range(1997,2012):
  print("You're in Generation Z")
elif birthyear in range(2013,2023):
  print("You're in Generation Alpha")
else:
  print("Try again")
              
