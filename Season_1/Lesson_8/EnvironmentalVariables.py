# Working with environmental variables to securly handle sensitive data

# With this module it is possible to read the system environment variables
import os
os_version = os.getenv("OS")
print(os_version)

# Another possibility is to store this things in a text file
# Only for Local purposes
# Adding the following package:
# pip install python-dotenv
from dotenv import load_dotenv
import os
load_dotenv()
database = os.getenv("DATABASE")
print(database)