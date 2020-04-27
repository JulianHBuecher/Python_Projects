# Handling different conditions

price = input("How much did you pay for this item: ")
price = float(price)

if price >= 1.00:
    tax = 0.7
else:
    tax = 0

print("You have to pay tax of "+str(tax))

# Comparing string

homecountry = input("Enter your home country: ")
if homecountry.lower() == "canada":
    print("So you must like hockey!")
else:
    print("You are not from Canada!")