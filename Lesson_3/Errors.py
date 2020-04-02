# Functions and tricks to handle errors
x = 42
y = 206
if x == y:
    print("Success")
else:
    print("Failure")

x = 42
y = 0

try:
    print(x / y)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print("Sorry, something went wrong!")
    print("Error Message:",e.args)
except:
    print("Something really went wrong")
finally:
    print("This always runs on success or failure")