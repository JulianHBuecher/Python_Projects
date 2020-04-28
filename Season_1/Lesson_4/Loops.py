# Usage of Loops in Python

# For-Loop with a fixed array
for index in [0,1]:
    print(index)

# For-Loop with an array created by range-operator
for index in range(0,2):
    print(index)

# While-Loop with condition
names = ["Christopher","Susan"]
index = 0
while index < len(names):
    print(names[index])
    index += 1

for name in names:
    print(name)

