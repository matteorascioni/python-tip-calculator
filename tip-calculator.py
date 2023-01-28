total_bill = float(input("What's your total bill?\n"))
total_percentage = int(input("What Percentage would you like to give? 10, 12, or 15 ?\n"))
total_people = int(input("How many people to split the bill ?\n"))

total_bill_splitted = total_bill / total_people
total_bill_splitted += total_bill_splitted * total_percentage / 100 
total_amount = round(total_bill_splitted, 2)
total_amount = "{:.2f}".format(total_bill_splitted)

print(f"The bill is {total_bill}$.\nIf you split in {total_people}, makes {total_amount}$ for each which includes the tips of {total_percentage}%")