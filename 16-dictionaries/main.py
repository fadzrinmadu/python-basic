"""
Dictionaries
"""

user_dictionary = {
  "username": "fadzrinmadu",
  "name": "Fadzrin",
  "age": 50,
}

user_dictionary["is_active"] = True

print(user_dictionary)
print(user_dictionary.get("username"))
print(len(user_dictionary))

for x, y in user_dictionary.items():
  print(x, y)


user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")

print(user_dictionary, user_dictionary2)
