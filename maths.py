print("Tip Calculator")
bill = float(input("How much did you spend?"))
TipPercentage = int(input("What percentage do you want to tip?"))
Totalpeople = int(input("How many people in your group?"))
Tip1 = TipPercentage / 100 * bill
Tip2 = Tip1 / Totalpeople
eachowe = bill/Totalpeople + Tip2
eachowe= round(eachowe,2)
print("You all owe", eachowe, "each")
