# Functions to work with string
sentence = "This is my cat Lili"
# Makes all the letters in the sentence to upper case
print(sentence.upper())
# Convert all the letters in the sentence to lower case
print(sentence.lower())
# Makes the first letter in the first word to upper case
print(sentence.capitalize())
# Counts the letter "i" in the sentence
print(sentence.count("i"))

# Example usage
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Hello "+first_name.capitalize()+" "+last_name.capitalize())

# Another formater for printing strings
# output = "Hello, {0} {1}!".format(first_name.capitalize(), last_name.capitalize())

# Streamlining the output with the build in format-function (only in Python 3)
output = f"Hello, {first_name} {last_name}"
print(output)