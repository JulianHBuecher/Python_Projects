def sorter(item):
    return item["name"]

presenters = [
    {"name":"Susan","age":50},
    {"name":"Christopher","age":47}
]

# presenters.sort(key=sorter)
# Alternative with Lambda functions
presenters.sort(key=lambda item: item["name"])

# For sorting with the number of characters the name used
presenters.sort(key=lambda item: len(item["name"]))

print(presenters)