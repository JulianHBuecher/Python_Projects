# Handling multiple conditions with if and elseif:

province = input("What's your home province: ")

if province.lower() == "alberta":
    tax = .05
elif province.lower() == "nunavut":
    tax = .05
elif province.lower() == "ontario":
    tax = .13
else:
    tax = .15

print("You have to pay a tax of "+str(tax))

# With the usage of the logical operator OR

province = input("What's your home province: ")

if province.lower() == "alberta" or province.lower() == "nunavut":
    tax = .05
elif province.lower() == "ontario":
    tax = .13
else:
    tax = .15

print("You have to pay a tax of "+str(tax))

# With the usage of the in-statement

province = input("What's your home province: ")

if province.lower() in ("alberta","nunavut","yukon"):
    tax = .05
elif province.lower() == "ontario":
    tax = .13
else:
    tax = .15

print("You have to pay a tax of "+str(tax))

# Make a bigger condition handling

country = input("What's your home country: ")
tax = 0

if country.lower == "canada":

    province = input("What's your home province: ")

    if province.lower() in ("alberta","nunavut","yukon"):
        tax = .05
    elif province.lower() == "ontario":
        tax = .13
    else:
        tax = .15
else:
    tax = 0.00

print("You have to pay a tax of "+str(tax))