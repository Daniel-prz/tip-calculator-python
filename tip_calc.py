bill = float(input('What is the total bill? '))
tip = int(input("What percentage do you want to tip - 10 12 15 etc. ? "))
people = int(input("How many people are splitting the bill? "))
tip_as_decimal = tip / 100
tip_amount = bill * tip_as_decimal
print(tip_as_decimal, tip_amount)
total_bill = bill + tip_amount
split = total_bill / people
print(f'Total = ${total_bill}. Tip = ${tip_amount}. Each pays ${split}.')