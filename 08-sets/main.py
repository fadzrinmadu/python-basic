"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly bracket
"""

my_sets = {1, 2, 3, 4, 5, 1, 2}
print(my_sets)
print(len(my_sets))

for x in my_sets:
  print(x)
  
my_sets.discard(3)
print(my_sets)

my_sets.add(6)
print(my_sets)

my_sets.update([7, 8])
print(my_sets)

my_sets.clear()
print(my_sets)
