# Usage of collections in Python

names = ["Christoper","Susan"]
scores = []

# Adding a new item at the end of the collection
scores.append(99)
scores.append(100)

# Print out the saved data
print(names)
print(scores)
# The collection in Python starts at 0
print(scores[1])

# Usage of arrays
from array import array

scores = array("d")
scores.append(99)
scores.append(100)
print(scores)
print(scores[0])

# Common operations for a array
names = ["Susan","Christopher"]
# Get the number of items btw. length of the array
print("The length of the array is: "+str(len(names)))
# Insert a new value before the index
names.insert(0,"Bill")
print("The length of the array is: "+str(len(names)))
print(names)
names.sort()
print(names)

# Getting a specific range of a collection
names = ["Susan","Christopher","Bill","Justin"]
# Start and end index for selection
# It will get "Christopher" and "Bill"
# The range operation set the indexes directly on the commas and square brackets
# So the 3. Index will end at the comma in front of "Justin", so "Justin" is not included anymore
presenters = names[1:3]
# Also possible
presenters = names[:3]

print(names)
print(presenters)

# Dictionaries
# Represents groups of key-value pairs
person = {"first":"Christopher"}
# Adding a additional person into the dictionary
person["last"] = "Harrison"
print(person)
print(person["first"])

chrisopher = {}
chrisopher["first"] = "Christopher"
chrisopher["last"] = "Harrison"

susan = {}
susan["first"] = "Susan"
susan["last"] = "Ibach"

people = []
people.append(chrisopher)
people.append(susan)
people.append({
    "first":"Bill", "last":"Gates"
})


print(people)