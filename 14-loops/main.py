"""
For & While Loops
"""

# For loop
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday"]
for x in my_list:
  print(f"Happy {x}")


# While loop
i = 0
while i < 5:
  i += 1
  if i == 3:
    continue
  print(i)
else:
  print("i is now larger or equal to 5")
