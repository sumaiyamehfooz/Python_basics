#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
Total = float(input(print("what was the toatl bill?")))
Tip = int(input(print("how much tip would you like to give? 10, 12, or 15?")))
Split = int(input(print("how many people to split the bill")))
Tip_as_percent = float(Tip / 100)
Total_tip_amount = float(Total * Tip_as_percent)
Total_bill = float(Total + Total_tip_amount)
Bill_per_person = round((Total_bill / Split), 2)
print(f"each person Should pay: ${Bill_per_person}")
