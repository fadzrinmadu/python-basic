"""
- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list
- Print all animals
- Print only the first 3 animals
"""

zoo = ["Monkey", "Zebra", "Gorilla", "Lion", "Tiger"]
zoo.pop(3)
zoo.append("Lizard")
zoo.pop(0)
print(zoo)

for x in zoo:
  print(x)
  
print(zoo[0:3])
