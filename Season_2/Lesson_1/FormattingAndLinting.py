# PEP 8
# Python Enhancement Proposal #8
# Includes all rules about formatting
# - Spaces, not tabs
# - variable_name, not variableName or VariableName
# - Avoid extraneous whitespace {"good":42}

# For identification of formatting issues you could install Pylint for Python
# Windows
# pip install pylint
# macOS or Linux
# pip3 install pylint
# It is possible to ignore certain rules, but you should avoid doing this
# Another benefit is, that it is automatically run by Visual Studio Code

name = input("What is your name? ")
# Comes from TypeScript
def print_hello(name: str) -> str:
    # return "Hello, " + name
    """
    Greets ths user by name

    Parameters:
        name (str): The name of the user
    Returns:
        str: The greeting
    """
    print("Hello, "+name)