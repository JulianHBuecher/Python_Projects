# Introduction of modules for usage in code

# By default the Python Package Installer PIP install all packages globally
# For many projects this is not necessary (because of versioning problems with other projects)
# For this case we could initialize virtual environments
# A virtual environment is just a simple folder with all code the application needed to run
# For creating virtual environments we need the tool: virtualenv
# To install it and initilize the environment use the following commands:
# pip install virtualenv
# To create the virtual environment
# Windows
# python -m venv <folder_name>
# Mac and Linux
# virtualenv <folder_name>

# To activate the virtual environment on Windows:
# cmd.exe
# <folder_name>\Scripts\Activate.bat
# Powershell
# <folder_name>\Scripts\Activate.ps1
# bash shell
# . ./<folder_name>/Scripts/activate

# To activate the virtual environment on OSX/Linux:
# <folder_name>/bin/activate

# Installing packages into a virtual environment 
# Install an individual package
# pip install colorama
# Install from a list of packages
# pip install -r requirements.txt
# Content of requirements.txt
# colorama