# list
numberList = []

for i in range(10):
  numberList.append(i)

print(numberList)

# tuple
myTuple = (True, 23, "Hello", [1, 2, 3])

for i in range(len(myTuple)-1):
  print(myTuple[i])

myList = ["a", "b", "c"]
copy = [*myList]

copy.pop(0)

print(myList)
print(copy)

# dict

myDictionary = {
  "person1": "kris",
  "person2": "tom",
  "person3": "pat"
}

for key, value in myDictionary.items():
  print(f'{key}: {value}')

for value in myDictionary.values():
  print(value)

for key in myDictionary:
  print(key)

print('\n' * 3)

# set
noDuplicatesAllowed = {"apple", "banana", "orange", "apple", "apple"}

for i in range(1, 4):
  noDuplicatesAllowed.add(i)

if "nonExistingElement" in noDuplicatesAllowed:
  noDuplicatesAllowed.remove("nonExistingElement")
else:
  print("Could not find the element you wanted to remove")

noDuplicatesAllowed.remove(3)


for setItem in noDuplicatesAllowed:
  print(setItem)

